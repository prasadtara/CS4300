from django.test import TestCase
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Movie, Seat, Booking

User = get_user_model()


# -------------------------
# UNIT TESTS (models only)
# -------------------------
class ModelUnitTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Movie1",
            description="Desc",
            release_date="2026-03-05",
            duration=120,
        )

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Movie1")

    def test_unique_seat_number_per_movie(self):
        Seat.objects.create(movie=self.movie, seat_number="A1")
        with self.assertRaises(IntegrityError):
            Seat.objects.create(movie=self.movie, seat_number="A1")

    def test_same_seat_number_allowed_for_different_movies(self):
        m2 = Movie.objects.create(
            title="Movie2",
            description="Desc2",
            release_date="2026-03-06",
            duration=90,
        )
        Seat.objects.create(movie=self.movie, seat_number="A1")
        Seat.objects.create(movie=m2, seat_number="A1")  # should not raise

    def test_booking_str_uses_name_or_anonymous(self):
        seat = Seat.objects.create(movie=self.movie, seat_number="B2")
        booking = Booking.objects.create(movie=self.movie, seat=seat, name="Alice")
        self.assertEqual(str(booking), "Alice - Movie1 - B2")

        seat2 = Seat.objects.create(movie=self.movie, seat_number="B3")
        booking2 = Booking.objects.create(movie=self.movie, seat=seat2, name="")
        self.assertEqual(str(booking2), "Anonymous - Movie1 - B3")

    def test_booking_date_autoset(self):
        seat = Seat.objects.create(movie=self.movie, seat_number="C1")
        booking = Booking.objects.create(movie=self.movie, seat=seat, name="Bob")
        self.assertIsNotNone(booking.booking_date)
        self.assertLess((timezone.now() - booking.booking_date).total_seconds(), 5)


# -----------------------------------------
# INTEGRATION TESTS (HTTP endpoints / API)
# -----------------------------------------
class IntegrationTests(APITestCase):
    MOVIES_URL = "/api/movies/"
    BOOKINGS_URL = "/api/bookings/"

    def setUp(self):
        # If your permissions are IsAuthenticated / IsAdminUser, this prevents 403.
        self.user = User.objects.create_user(
            username="testuser",
            password="pass123",
            is_staff=True,
        )
        self.client.force_authenticate(user=self.user)

        self.movie = Movie.objects.create(
            title="Movie API",
            description="API Desc",
            release_date="2026-03-05",
            duration=120,
        )
        self.seat = Seat.objects.create(movie=self.movie, seat_number="A1")

    def test_movies_list_endpoint(self):
        resp = self.client.get(self.MOVIES_URL)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        data = resp.data
        if isinstance(data, dict) and "results" in data:
            data = data["results"]

        titles = [item.get("title") for item in data]
        self.assertIn("Movie API", titles)

    def test_create_booking_endpoint_books_a_seat(self):
        payload = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "name": "Test Booker",
        }

        resp = self.client.post(self.BOOKINGS_URL, payload, format="json")
        self.assertIn(resp.status_code, (status.HTTP_201_CREATED, status.HTTP_200_OK))
        self.assertEqual(Booking.objects.count(), 1)

    def test_cannot_double_book_same_seat(self):
        Booking.objects.create(movie=self.movie, seat=self.seat, name="First")

        payload = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "name": "Second",
        }

        resp = self.client.post(self.BOOKINGS_URL, payload, format="json")
        self.assertIn(resp.status_code, (status.HTTP_400_BAD_REQUEST, status.HTTP_409_CONFLICT))
        self.assertEqual(Booking.objects.count(), 1)