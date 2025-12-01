from django.contrib import admin
from .models import Language, Location, Movie

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'location', 'release_date', 'rating')
    list_filter = ('language', 'location', 'release_date')
    search_fields = ('title', 'description')
