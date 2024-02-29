from django.shortcuts import render
from .models import *

def home(request):
    cars = Car.objects.all()
    for car in cars:
        if car.id % 2 != 0:
            car.delete()
    for car in cars:  
        car.name = f"{car.id}.{car.name}"
    return render(request, 'home.html', {'cars': cars})
