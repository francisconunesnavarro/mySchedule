from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import LoginView
from django.contrib import admin

from myschedule.accounts import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^entrar/$', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    url(r'^sair/$', logout_then_login,{'login_url': 'accounts:login'}, name="logout"),
    url(r'^cadastre-se/$', views.register, name='register'),
]
