from django.urls import path
from . import web_views

urlpatterns = [
    path("movies/", web_views.movie_list, name="movie_list"),
    path("movies/<int:movie_id>/seats/", web_views.movie_seats, name="movie_seats"),
    path("my-bookings/", web_views.booking_history, name="booking_history"),
    path("my-bookings/delete/<int:booking_id>/", web_views.delete_booking, name="delete_booking"),
]
