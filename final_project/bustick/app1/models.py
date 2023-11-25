# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import date


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


from django.db import models


class Stop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Bus(models.Model):
    BUS_TYPE_CHOICES = [
        ('AC-Sleeper', 'AC-Sleeper'),
        ('Non-AC-Sleeper', 'Non-AC-Sleeper'),
        ('AC-seater', 'AC-seater'),
        ('Non-AC-seater', 'Non-AC-seater'),
    ]
    name = models.CharField(max_length=100)
    total_seats = models.IntegerField(default=50)  # Assume 50 seats by default
    available_seats = models.IntegerField(default=50)  #
    boarding_stops = models.ManyToManyField(Stop, through='BoardingStop', related_name='boarding_buses')
    destination_stops = models.ManyToManyField(Stop, through='DestinationStop', related_name='destination_buses')
    bus_type = models.CharField(max_length=30, choices=BUS_TYPE_CHOICES, default='Non-AC-Non-Sleeper')

    def __str__(self):
        return self.name


from datetime import datetime, timedelta


class BoardingStop(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    departure_time = models.TimeField(default=20)
    distance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.bus} - Boarding at {self.stop} - Departure: {self.departure_time}"


class DestinationStop(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    arrival_time = models.TimeField(default=8)
    distance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.bus} - Destination: {self.stop} - Arrival: {self.arrival_time}"


class BookedSeat(models.Model):
    bus_id = models.CharField(max_length=100, default='YourDefaultValueHere')
    date = models.DateField(default=date.today)
    seat_number = models.CharField(max_length=10)
    passenger_name = models.CharField(max_length=100, default='Unknown')
    passenger_gender = models.CharField(max_length=10, default='Unknown')
    status = models.CharField(max_length=10, default='unknown')

    def __str__(self):
        return f"Bus ID: {self.bus_id}, Seat Number: {self.seat_number}, Date: {self.date}, Passenger: {self.passenger_name}, Gender: {self.passenger_gender}, Status: {self.status}"
