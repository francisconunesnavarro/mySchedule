from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status, viewsets


from myschedule.accounts.models import User
from myschedule.core.serializers import UserSerializer
from myschedule.schedules.models import Schedule

User = get_user_model()


@login_required
def home(request):
    schedule = Schedule.objects.all()
    template_name = 'schedules/index.html'
    context = {
        'schedules':schedule
    }

    return render(request, template_name, context)

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @list_route()
    def recent_users(self, request):
        recent_users = User.objects.all().order('-last_login')

        page = self.paginate_queryset(recent_users)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        
        return Response(serializer.data)

