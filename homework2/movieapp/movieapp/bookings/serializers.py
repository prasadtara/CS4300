from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Movie, Seat, Booking

User = get_user_model()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "release_date", "duration"]


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ["id", "seat_number", "is_booked"]


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "movie", "seat", "user", "booking_date"]
        read_only_fields = ["user", "booking_date"]
