from django.conf.urls import include, url
from django.contrib import admin
from locations.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
]
