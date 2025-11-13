# bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
 booking-page
    path('create/<int:destination_id>/', views.create_booking, name='create_booking')
]
