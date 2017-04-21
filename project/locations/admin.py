from django.contrib import admin
from .models import *


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"iso": ("name",)}
    list_display = ('name', 'nationality', 'iso',)
    ordering = ('name',)
admin.site.register(Country, CountryAdmin)


class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"iso": ("name",)}
    list_display = ('name', 'iso', 'country',)
    ordering = ('iso',)
admin.site.register(Region, RegionAdmin)


class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'region', 'get_country', 'slug',)
    def get_country(self, obj):
        return obj.region.country
    get_country.short_description = 'Country'
    search_fields = ['name', 'slug',]
    ordering = ('slug',)
admin.site.register(City, CityAdmin)


class VenueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'city', 'get_country',)
    def get_country(self, obj):
        return obj.city.region.country
    get_country.short_description = 'Country'
    search_fields = ['name', 'slug',]
    ordering = ('slug',)
admin.site.register(Venue, VenueAdmin)


class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'city', 'get_country',)
    def get_country(self, obj):
        return obj.city.region.country
    get_country.short_description = 'Country'
    search_fields = ['name', 'slug',]
    ordering = ('slug',)
admin.site.register(Team, TeamAdmin)
