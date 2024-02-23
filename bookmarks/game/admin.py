from django.contrib import admin
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['sport', 'amount_players', 'place', 'created']
    list_filter = ['created']
