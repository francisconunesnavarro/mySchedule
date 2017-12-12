from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from myschedule.core import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include(router.urls)),
]
