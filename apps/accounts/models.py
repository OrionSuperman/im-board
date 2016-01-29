from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.apps import apps


class Info(models.Model):
	bio = models.CharField(max_length=200, default="Bio is not Set")
	
	games = models.ManyToManyField(apps.get_app_config('games').models['game'])

	# games = models.ManyToManyField(apps.get_app_config('games').models['game'])

	info_user = models.OneToOneField(User)
	class Meta:
		db_table = 'infos'	

class Address(models.Model):
	street1 = models.CharField(max_length=100, default="")
	steet2 = models.CharField(max_length=100, default="")
	city = models.CharField(max_length=100, default="")
	state = models.CharField(max_length=2, default="")
	zipcode = models.IntegerField()
	user = models.OneToOneField(Info)

