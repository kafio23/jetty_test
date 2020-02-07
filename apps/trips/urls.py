from django.urls import path
from . import views

urlpatterns = [
    path('', views.trips_list, name='trips_list')
]
