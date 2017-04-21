from django.contrib import admin
from .models import *


class AliasAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug',)
    search_fields = ['name', 'slug']
    ordering = ('slug',)
admin.site.register(Alias, AliasAdmin)


class RefereeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug',)
    search_fields = ['name', 'slug']
    ordering = ('slug',)
admin.site.register(Referee, RefereeAdmin)


class TrainerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug',)
    search_fields = ['name', 'slug']
    ordering = ('slug',)
admin.site.register(Trainer, TrainerAdmin)


class FighterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("birth_name",)}
    list_display = ('birth_name', 'get_alias', 'get_nationality', 'get_team', 'twitter',)
    def get_alias(self, obj):
        aliases = []
        for alias in obj.alias.all():
            aliases.append(alias)
        return aliases
    get_alias.short_description = 'Alias'
    def get_team(self, obj):
        teams = []
        for team in obj.team.all():
            teams.append(team)
        return teams
    get_team.short_description = 'Team'
    def get_nationality(self, obj):
        nats = []
        for nat in obj.nationality.all():
            nats.append(nat)
        return nats
    get_nationality.short_description = 'Nationality'
    search_fields = ['first_name', 'slug',]
    list_filter = ['sex', 'stance', 'nationality']
    ordering = ('slug',)
admin.site.register(Fighter, FighterAdmin)
