from django import forms
from django.conf import settings

from .models import Schedule

class InsertScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['name', 'date_schedule', 'date_schedule_start', 'date_schedule_end', 'procedure']
        
class EditScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['name', 'date_schedule', 'date_schedule_start', 'date_schedule_end', 'procedure']