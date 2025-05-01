from rest_framework import serializers
from .models import Itinerary, Day, Hotel, Activity, Transfer

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

class DaySerializer(serializers.ModelSerializer):
    transfers = TransferSerializer(many=True, read_only=True)
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = '__all__'

class ItinerarySerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = '__all__'
