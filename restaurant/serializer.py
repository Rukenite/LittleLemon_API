from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '_all_'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '_all_'
