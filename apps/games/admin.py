from django.contrib import admin

from .models import Game, GameType

admin.site.register(Game)
admin.site.register(GameType)