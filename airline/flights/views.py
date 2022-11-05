from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Flight, Passenger, Airport

# Create your views here.
def index(request):
    return render(request, 'flights/index.html', {
        'Flights': Flight.objects.all()
    })

def port(request):
    return render(request, 'flights/roporo.html',{
        'Airports': Airport.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, 'flights/flight.html', {
        'flight':flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights = flight).all()
        #what this line does, it will exclude all passenger that have fligths and take the remaing ones.
    })


def book(request, flight_id):
    if request.method == 'POST':
        #this line means that if they try to book for that person, the flight number will be that of the one booking Or that in in which page we're in
        flight = Flight.objects.get(pk = flight_id)
        #what this line mean it that, when the for for is submitted, the passenger information will be gottem from pk corresponding to the one submitted
        passenger = Passenger.objects.get(pk = int(request.POST['passenger']))
        #and here the passene is added
        passenger.flights.add(flight)
        #what this means is that after booking the flight, I am redirecting them the page showing flight imformation and passengers in it
        return HttpResponseRedirect(reverse('flight', args=(flight.id,)))