from __future__ import unicode_literals

from django.db import models


class GameType(models.Model):
	category = models.TextField(max_length=50)
	category_description = models.TextField()
	

	def __str__(self):
		return self.category
	class Meta: 
		db_table = 'gametypes'
		ordering = ('category',)

class Game(models.Model):
	game_title = models.TextField(max_length=255)
	game_image = models.CharField(max_length=255)
	game_description = models.TextField()
	min_players = models.FloatField()
	max_players = models.IntegerField()
	game_length = models.CharField(max_length=100)
	game_type = models.ManyToManyField(GameType)
	def __str__(self):
		return self.game_title
	class Meta:
		db_table = 'games'
		ordering = ('game_title',)