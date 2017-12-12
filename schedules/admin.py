from django.contrib import admin

from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):

    list_display = ['date_schedule', 'slug', 'date_schedule_start', 'date_schedule_end', 'name']
    search_fields = ['date_schedule', 'slug', 'name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Schedule, ScheduleAdmin)