# bookings/models.py
from django.db import models
from destinations.models import Destination

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='bookings')

    def __str__(self):
        return f"{self.name} - {self.destination.name}"
