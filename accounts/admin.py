from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'is_active', 'is_staff']
    search_fields = ['name', 'email']

admin.site.register(User, UserAdmin)