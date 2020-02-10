from django.urls import path
from . import views

urlpatterns = [
    path('<int:driver_id>/', views.driver, name='drivers_url')
]