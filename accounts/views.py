from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

from myschedule.accounts.forms import RegisterForm

User = get_user_model()


@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    context = {}
    
    return render(request, template_name, context)

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, 
                password=form.cleaned_data['password1']
            )
            login(request, user)
            
            return redirect('core:home')
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }

    return render(request, template_name, context)
