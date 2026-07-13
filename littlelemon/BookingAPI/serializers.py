from restaurant.models import Booking
from rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
    model = Booking
    Fields = '__all__'