from django.shortcuts import render
import requests as req


def trips_list(request):
    context = {}
    print(request)
    return render(request, "trips/trips_list.html", context)
