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
	host = models.ForeignKey(User)
	
	games = models.ManyToManyField(apps.get_app_config('games').models['game'])
	time = models.DateTimeField()
	seats = models.IntegerField()
	seats_filled = models.IntegerField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	################################################
	# to call these methods use **event_object**.model_name()
	################################################
	def get_participants(self):
		# returns all participants of the event.
		return self.participant_set.all()

	def get_seats_remaining(self):
		# get how many open spots there are left
		open_seats = self.seats - self.seats_filled
		return open_seats

	def get_event_location(self):
		return self.location_set.all()


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
	zipcode = models.IntegerField(default=99999)

	def __str__(self):
		return self.event.event_name
	class Meta:
		db_table = 'locations'


class Distance(models.Model):
	zipcode1 = models.IntegerField()
	zipcode2 = models.IntegerField()
	distance = models.FloatField()

	def within_distance(self, zipcode, dist):
		results = self.objects.filter(zipcode1 = zipcode).filter(distance__lte = dist)
		return results

	def get_distance(self, zipcode1, zipcode2):
		results = self.objects.filter(zipcode1 = zipcode1, zipcode2 = zipcode2)
		distance = results.distance
		return distance

	def __str__(self):
		return self.zipcode1
	class Meta:
		db_table = 'distances'


