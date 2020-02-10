from django.shortcuts import render
from .models import Driver
import requests as req


def driver(request, driver_id):
    context = {}
    drivers = Driver.objects.get(driver_id=driver_id)
    print(drivers.email)
    print(driver_id)

    return render(request, "drivers/trips_list.html", context)
