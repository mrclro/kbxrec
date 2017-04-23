from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^fighters/', views.FighterListView.as_view(), name='fighters'),
]
