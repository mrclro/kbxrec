from django.contrib import admin
from .models import *


class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'website',)
    search_fields = ['name',]
    ordering = ('slug',)
admin.site.register(Organization, OrganizationAdmin)


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'date', 'organization', 'venue', 'get_location')
    def get_location(self, obj):
        return obj.venue.city, obj.venue.city.region.country
    get_location.short_description = 'Location'
    search_fields = ['name', 'organization__name', 'slug',]
    list_filter = ['date',]
    ordering = ('slug',)
admin.site.register(Event, EventAdmin)


class CardAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("event","name",)}
    list_display = ('name', 'event', 'slug',)
    ordering = ('slug',)
admin.site.register(Card, CardAdmin)


class TitleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'organization', 'slug',)
    search_fields = ['name', 'organization__name', 'slug',]
    list_filter = ['organization',]
    ordering = ('slug',)
admin.site.register(Title, TitleAdmin)
