# bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:destination_id>/', views.create_booking, name='create_booking'),
]
