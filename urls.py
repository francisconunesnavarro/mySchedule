from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from myschedule.core import views


urlpatterns = [
    url(r'^', include('myschedule.core.urls', namespace='core')),
    url(r'^conta/', include('myschedule.accounts.urls', namespace='accounts')),
    url(r'^agenda/', include('myschedule.schedules.urls', namespace='schedules')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
