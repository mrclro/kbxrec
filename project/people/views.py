from django.views.generic import ListView
from .models import Fighter

class FighterListView(ListView):
    template_name = 'people/fighters.html'
    model = Fighter
