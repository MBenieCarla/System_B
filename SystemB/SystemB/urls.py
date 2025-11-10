from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # AppUsers app (home page routes)
    # path('', include('AppUsers.urls', namespace='AppUsers')),
    path ('', include('AppUsers.urls')),
    

    # Destinations app
    # path('destinations/', include('destinations.urls', namespace='destinations')),
    path ('destinations/', include('destinations.urls')),

    # Bookings app
    # path('bookings/', include('bookings.urls', namespace='bookings')),
    path('bookings/', include('bookings.urls')),
]
