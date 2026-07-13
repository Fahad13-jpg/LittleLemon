from django.shortcuts import render
from rest_framework import generics
from restaurant.models import Booking
from rest_framework.permissions import IsAuthenticated
from .serializers import BookingSerializer

# Create your views here.

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer