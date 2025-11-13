from django.urls import path
from . import views

app_name = "bookings"  # important if using namespace

urlpatterns = [
    path('create/<int:destination_id>/', views.create_booking, name='create_booking'),
]

