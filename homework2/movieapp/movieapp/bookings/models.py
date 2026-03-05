from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title


class Seat(models.Model):
    #Seats belong to a movie
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="seats")
    seat_number = models.CharField(max_length=10)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "seat_number"],
                name="unique_seat_per_movie",
            )
        ]

    def __str__(self):
        return f"{self.movie.title} - {self.seat_number}"


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="bookings")
    seat = models.OneToOneField(Seat, on_delete=models.PROTECT, related_name="booking")
    name = name = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        who = self.name or "Anonymous"
        return f"{who} - {self.movie.title} - {self.seat.seat_number}"