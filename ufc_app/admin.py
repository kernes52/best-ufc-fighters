from django.contrib import admin
from .models import Fighter, WeightClass, Event, Bout

class BoutInline(admin.TabularInline):
    model = Bout
    fk_name = 'event'
    extra = 1

@admin.register(WeightClass)
class WeightClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'min_weight', 'max_weight')
    search_fields = ('code', 'name')
    ordering = ('id',)

class BoutRedInline(admin.TabularInline):
    model = Bout
    fk_name = 'fighter_red'
    extra = 0

class BoutBlueInline(admin.TabularInline):
    model = Bout
    fk_name = 'fighter_blue'
    extra = 0

@admin.register(Fighter)
class FighterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'weight_class', 'wins', 'losses', 'stance')
    list_filter = ('weight_class', 'country', 'stance')
    search_fields = ('name',)
    inlines = [BoutRedInline, BoutBlueInline]
    ordering = ('id',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'city', 'country')
    list_filter = ('date', 'city', 'country')
    search_fields = ('title',)
    inlines = [BoutInline]
    ordering = ('-date',)

@admin.register(Bout)
class BoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'fighter_red', 'fighter_blue', 'result', 'method', 'round', 'time')
    list_filter = ('event', 'method', 'result', 'round')
    search_fields = ('fighter_red__name', 'fighter_blue__name')
    ordering = ('id',)
