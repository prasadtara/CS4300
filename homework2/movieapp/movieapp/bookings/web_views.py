from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db.models import IntegerField
from django.db.models.functions import Substr, Cast

from .models import Movie, Seat, Booking

@require_POST
def delete_booking(request, booking_id):
    name = (request.POST.get("name") or "").strip()
    booking = get_object_or_404(Booking, id=booking_id)

    
    if not name or booking.name.lower() != name.lower():
        messages.error(request, "Name mismatch. Cannot delete this booking.")
        return redirect(f"/my-bookings/?name={name}")

    booking.delete()
    messages.success(request, "Booking deleted.")
    return redirect(f"/my-bookings/?name={name}")

def movie_list(request):
    movies = Movie.objects.all().order_by("-release_date")
    return render(request, "bookings/movie_list.html", {"movies": movies})


def movie_seats(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = (
    Seat.objects.filter(movie=movie)
    .annotate(
        row_letter=Substr("seat_number", 1, 1),
        seat_num=Cast(Substr("seat_number", 2), IntegerField()),
    )
    .order_by("row_letter", "seat_num")
)

    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        name = (request.POST.get("name") or "").strip()  # ✅ read name

        with transaction.atomic():
            seat = Seat.objects.select_for_update().get(id=seat_id, movie=movie)

            if Booking.objects.filter(seat=seat).exists():
                messages.error(request, "Seat already booked.")
                return redirect("movie_seats", movie_id=movie.id)

            Booking.objects.create(movie=movie, seat=seat, name=name)  # ✅ save name

        messages.success(request, f"Booked seat {seat.seat_number}!")
        # optional: send them to history filtered by name
        if name:
            return redirect(f"/my-bookings/?name={name}")
        return redirect("movie_seats", movie_id=movie.id)

    return render(request, "bookings/seat_booking.html", {"movie": movie, "seats": seats})

def booking_history(request):
    name = (request.GET.get("name") or "").strip()

    bookings = []
    if name:
        bookings = (
            Booking.objects.select_related("movie", "seat")
            .filter(name__iexact=name)
            .order_by("-booking_date")
        )

    return render(request, "bookings/booking_history.html", {"bookings": bookings, "name": name})