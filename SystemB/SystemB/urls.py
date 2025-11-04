from django.contrib import admin
from django.urls import path,include
 
app_name = 'AppUsers'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('AppUsers.urls')), 
]