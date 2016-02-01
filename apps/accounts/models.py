from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.apps import apps


Game = apps.get_app_config('games').models['game']
# Zipcode = apps.get_app_config('zipcodes').models['distance']
GameType = apps.get_app_config('games').models['gametype']
# Event = apps.get_app_config('events').models['event']


class Address(models.Model):
	street1 = models.CharField(max_length=100, default="none")
	street2 = models.CharField(max_length=100, default="none")
	city = models.CharField(max_length=100, default="none")
	state = models.CharField(max_length=2, default="none")
	zipcode = models.IntegerField()
	# user = models.OneToOneField(Info)


class Info(models.Model):
	bio = models.CharField(max_length=200, default="Bio is not Set")
	info_user = models.OneToOneField(User)
	user_address = models.OneToOneField(Address)
	games = models.ManyToManyField(Game)
	reviews = models.ManyToManyField('self', through='Review', symmetrical=False, related_name='related_to')

	def get_user_zipcode(self):
		return self.user_address.zipcode

	def __str__(self):
		return self.info_user.username
	class Meta:
		db_table = 'infos'	


class Review(models.Model):

	review_by = models.ForeignKey(Info, related_name='reviews_by')
	review_for = models.ForeignKey(Info, related_name='reviews_for')
	review = models.TextField()
	rating = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.review
	class Meta:
		db_table = 'reviews'
	
	#still need to add more for the rating field for 1-5.

	



