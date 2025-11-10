from django.shortcuts import render, redirect
from .models import Booking, Destination  # or whatever models you have
from .forms import BookingForm  # if you have a form
from .models import Booking, Destination


def create_booking(request, destination_id):
    # Example logic
    destination = Destination.objects.get(id=destination_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.destination = destination
            booking.save()
            return redirect('some_view_name')  # redirect somewhere
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form, 'destination': destination})
