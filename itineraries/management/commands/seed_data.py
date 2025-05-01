from django.core.management.base import BaseCommand
from itineraries.models import Hotel, Itinerary, Day, Transfer, Activity

class Command(BaseCommand):
    help = "Seed the database with the sample data for Phuket and Krabi"

    def handle(self, *args, **kwargs):
        Hotel.objects.all().delete()
        Itinerary.objects.all().delete()
        Day.objects.all().delete()
        Transfer.objects.all().delete()
        Activity.objects.all().delete()

        # Create hotels
        hotel_phuket = Hotel.objects.create(name="Phuket Beach Resort", location="Patong Beach")
        hotel_krabi = Hotel.objects.create(name="Krabi Island Retreat", location="Ao Nang Beach")

        # Create itinerary
        itinerary = Itinerary.objects.create(name="Phuket to Krabi Adventure", nights=5, region="Thailand")

        # Create days
        day1 = Day.objects.create(day_number=1, itinerary=itinerary, hotel=hotel_phuket)
        day2 = Day.objects.create(day_number=2, itinerary=itinerary, hotel=hotel_krabi)

        # Create activities
        Activity.objects.create(name="Island Boat Tour", description="Explore the scenic Island.", day=day1, hotel=hotel_phuket)
        Activity.objects.create(name="Snorkeling", description="Discover underwater life.", day=day2, hotel=hotel_krabi)

        # Create transfer
        Transfer.objects.create(from_location=hotel_phuket, to_location=hotel_krabi, mode="Bus", day=day2)

        self.stdout.write(self.style.SUCCESS('Successfully Done'))
