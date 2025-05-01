from django.test import TestCase
from itineraries.models import Itinerary, Day, Hotel, Transfer

class ItineraryTests(TestCase):
    def setUp(self):
        self.hotel = Hotel.objects.create(name="Phuket Beach Resort", location="Patong Beach")
        self.itinerary = Itinerary.objects.create(name="Phuket Adventure", nights=5, region="Thailand")
    
    def test_itinerary_creation(self):
        self.assertEqual(self.itinerary.name, "Phuket Adventure")
        self.assertTrue(2 <= self.itinerary.nights <= 8) 
        
    def test_day_creation(self):
        day = Day.objects.create(day_number=1, itinerary=self.itinerary, hotel=self.hotel)
        self.assertEqual(day.day_number, 1)
        self.assertEqual(day.itinerary.name, "Phuket Adventure")
        self.assertEqual(day.hotel.name, "Phuket Beach Resort")

class TransferTests(TestCase):
    def setUp(self):
        self.hotel1 = Hotel.objects.create(name="Hotel A", location="Location A")
        self.hotel2 = Hotel.objects.create(name="Hotel B", location="Location B")
        self.itinerary = Itinerary.objects.create(name="Test Itinerary", nights=3, region="Thailand")
        self.day = Day.objects.create(day_number=1, itinerary=self.itinerary, hotel=self.hotel1)

    def test_valid_transfer(self):
        transfer = Transfer.objects.create(
            from_location=self.hotel1,
            to_location=self.hotel2,
            mode="Bus",
            day=self.day
        )
        self.assertEqual(transfer.mode, "Bus")

    def test_invalid_transfer_same_location(self):
        with self.assertRaises(ValueError):
            Transfer.objects.create(
                from_location=self.hotel1,
                to_location=self.hotel1,
                mode="Bus",
                day=self.day
            )
    