from django.conf.urls import url, include
from django.contrib import admin

from myschedule.schedules import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cadastrar/$', views.insert, name='insert'),
    url(r'^(?P<pk>[\w_-]+)/$', views.details, name='details'),
    url(r'^(?P<pk>[\w_-]+)/editar/$', views.edit, name='edit'),
    url(r'^(?P<pk>[\w_-]+)/deletar/$', views.delete, name='delete'),
]
