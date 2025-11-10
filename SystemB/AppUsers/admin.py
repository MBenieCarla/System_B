from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'created_at']
    search_fields = ['fullname', 'email']
    list_filter = ['created_at']

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.site_header = "System B Admin"
admin.site.site_title = "System B Portal"
admin.site.index_title = "Welcome to System B Admin Dashboard"