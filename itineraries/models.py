from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name} -- {self.location}"

    

class Itinerary(models.Model):
    name = models.CharField(max_length=255)
    nights = models.IntegerField()
    region = models.CharField(max_length=150)
    
    def clean(self):
        if not(2 <= self.nights <= 8):
            raise ValueError("Itineraries must be between 2 and 8 nights.")

    def __str__(self):
        return f"{self.name} -- ({self.nights} nights) -- {self.region}"
    
class Day(models.Model):
    day_number = models.IntegerField()
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name="days")
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f" {self.day_number} days of {self.itinerary.name} in the {self.hotel} hotel"

class Transfer(models.Model):
    TRANSPORT_MODES = [("Flight", "Flight"), ("Train", "Train"), ("Bus", "Bus"), ("Car", "Car"), ("Boat", "Boat")]
    from_location = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="transfer_from")
    to_location = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="transfer_to")
    mode = models.CharField(max_length=50, choices=TRANSPORT_MODES, default="Car")
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="transfers")
    
    class Meta:
        indexes = [
            models.Index(fields=["from_location"]),
            models.Index(fields=["to_location"]),
            models.Index(fields=["mode"]),
        ]

    def clean(self):
        super().clean()
        if self.from_location == self.to_location:
            raise ValueError("From location and To location cannot be the same.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transfer from {self.from_location} to {self.to_location}"


class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="activities")
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, related_name="activities")

    def __str__(self):
        return f"{self.name} (Days {self.day.day_number} - {self.day.itinerary.name}, Hotel:{self.hotel.name if self.hotel else "No hotel"})"
    


