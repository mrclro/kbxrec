from django.contrib import admin
from .models import *


class MatchAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_event', 'method', 'draw', 'no_contest')

    def get_event(self, obj):
        return obj.card.event
    get_event.short_description = 'Event'

    search_fields = ['figter1', 'fighter2', 'card__event',]
    list_filter = ['weight_max', 'draw', 'no_contest']
    ordering = ('-card__event__date',)
admin.site.register(Match, MatchAdmin)
