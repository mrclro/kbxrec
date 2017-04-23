from django.conf.urls import include, url
from django.contrib import admin
from index.views import IndexTemplateView

urlpatterns = [
    url(r'^$', IndexTemplateView.as_view(), name='index'),
    url(r'^people/', include('people.urls')),
    url(r'^admin/', admin.site.urls),
]
