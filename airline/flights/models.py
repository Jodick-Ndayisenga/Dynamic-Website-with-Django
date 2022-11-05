from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.city}({self.code})'


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='Departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='Arrivals')
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.origin} to {self.destination} in {self.duration}min'


class Passenger(models.Model):
    firstName = models.CharField(max_length=64)
    secondName = models.CharField(max_length=64)
    phone = models.IntegerField()
    flights = models.ManyToManyField(Flight, blank = True, related_name='passengers')

    def __str__(self):
        return f'{self.firstName} {self.secondName} Tel: {self.phone}'