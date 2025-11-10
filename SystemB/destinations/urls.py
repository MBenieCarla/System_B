from django.urls import path
from . import views  # import views from the same app

# Namespace for this app (used in templates and redirects)
app_name = 'destinations'

urlpatterns = [
    # URL to show all destinations
    path('', views.destination_list, name='list'),

    # URL to show a single destination's details
    path('<int:pk>/', views.destination_detail, name='detail'),
]
