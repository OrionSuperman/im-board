from __future__ import unicode_literals
from django.apps import apps
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import datetime
# from apps.games.models import Game, GameType
from django.utils import timezone

Game = apps.get_app_config('games').models['game']
Info = apps.get_app_config('accounts').models['info']




class Event(models.Model):
	event_name = models.CharField(max_length=50)
	host = models.ForeignKey(User, default = User.objects.get(id=22))
	
	games = models.ManyToManyField(apps.get_app_config('games').models['game'])
	time = models.DateTimeField()
	seats = models.IntegerField()
	seats_filled = models.IntegerField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.event_name
	class Meta:
		db_table = 'events'	


class Participant(models.Model):
	participant = models.ForeignKey(User)
	contact = models.CharField(max_length=100)
	event = models.ForeignKey(Event)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.participant.username
	class Meta:
		db_table = 'participants'

class Location(models.Model):
	event = models.OneToOneField(Event)
	street1 = models.CharField(max_length=100, default="")
	street2 = models.CharField(max_length=100, default="")
	city = models.CharField(max_length=100, default="")
	state = models.CharField(max_length=2, default="")
	zipcode = models.IntegerField()

	def __str__(self):
		return self.event.event_name
	class Meta:
		db_table = 'locations'