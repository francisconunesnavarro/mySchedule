from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Schedule
from .forms import InsertScheduleForm, EditScheduleForm

@login_required
def index(request):
    
    schedule = Schedule.objects.all()
    template_name = 'schedules/index.html'
    context = {
        'schedules':schedule
    }

    return render(request, template_name, context)

@login_required
def details(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    context = {
        'schedule': schedule,
    }
    template_name = 'schedules/details.html'

    return render(request, template_name, context)

@login_required
def insert(request):
    template_name = 'schedules/insert.html'
    schedule = Schedule()
    context = {}

    if request.method == 'POST':
        form = InsertScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            if schedule.date_schedule_end <= schedule.date_schedule_start:
                messages.error(request, 'A hora final tem que ser maior que a hora inicial')
            else:
                schedule.slug = schedule.name.lower().replace(' ', '-')
                form.save()
                
                return (redirect('schedules:index'))
    else:
        form = InsertScheduleForm(instance=schedule)
    
    context = {
        'form': form,
        'schedule': schedule,
    }
    
    return render(request, template_name, context)

@login_required
def edit(request, pk):
    template_name = 'schedules/edit.html'
    schedule = get_object_or_404(Schedule, pk=pk)
    context = {}

    if request.method == 'POST':
        form = EditScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            if schedule.date_schedule_end <= schedule.date_schedule_start:
                messages.error(request, 'A hora final tem que ser maior que a hora inicial')
            else:
                form.save()
                
                return (redirect('schedules:index'))
    else:
        form = EditScheduleForm(instance=schedule)
    
    context = {
        'form': form,
        'schedule': schedule,
    }

    return render(request, template_name, context)

@login_required
def delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    context = {}

    if request.method == 'POST':
        schedule.delete()
        
        return (redirect('schedules:index'))
    
    template_name = 'schedules/delete.html'
    context = {
        'schedule': schedule,
    }

    return render(request, template_name, context)
