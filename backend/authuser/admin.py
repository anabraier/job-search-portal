from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'updated_at')  # Fields to display in list view
    # list_filter = ('created_at', 'updated_at')  # Fields to filter by in list view
    # search_fields = ('name', 'description')  # Fields to search by in list view
    # ordering = ('-created_at',)  # Default ordering of the list view
    # readonly_fields = ('created_at', 'updated_at')  

admin.site.register(User, UserAdmin)