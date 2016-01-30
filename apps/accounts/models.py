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
	street1 = models.CharField(max_length=100, default="")
	street2 = models.CharField(max_length=100, default="")
	city = models.CharField(max_length=100, default="")
	state = models.CharField(max_length=2, default="")
	zipcode = models.IntegerField()
	# user = models.OneToOneField(Info)


class Info(models.Model):
	bio = models.CharField(max_length=200, default="Bio is not Set")
	info_user = models.OneToOneField(User)
	address = models.OneToOneField(Address)
	games = models.ManyToManyField(Game)
	class Meta:
		db_table = 'infos'	


class Review(models.Model):

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	review = models.TextField()
	rating = models.CharField(max_length=1)
	#still need to add more for the rating field for 1-5.
	review_by = models.ForeignKey(User, related_name='review_by')
	# review_for = models.ForeignKey(User)

class User_Profile_Review(Review):
	user_id = models.ForeignKey(User, related_name='review_for')

