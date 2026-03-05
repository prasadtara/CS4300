from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        """
        A seat is considered 'booked' if it already has a Booking linked to it.
        Because Booking.seat is OneToOneField(Seat, related_name="booking").
        """
        seat = serializer.validated_data["seat"]

        # If a Booking already exists for this seat, Seat will have the reverse relation.
        if hasattr(seat, "booking"):
            raise ValidationError({"seat": "This seat is already booked."})

        serializer.save()

    # If you already had a custom create(), you can keep it.
    # DRF's default create() is fine, but this keeps behavior explicit.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)