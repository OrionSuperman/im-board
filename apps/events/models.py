from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Event(models.Model):
	event_name = models.CharField(max_length=50)
	# host = models.ForeignKey(User)
	game = models.CharField(max_length=50)
	time = models.DateTimeField()
	seats = models.IntegerField()
	description = models.TextField()
	class Meta:
		db_table = 'events'	


class Participant(models.Model):
	first_name = models.CharField(max_length=50)
	birthday = models.DateField(auto_now=False)
	contact = models.CharField(max_length=32)
	bio = models.TextField()
	class Meta:
		db_table = 'participants'


	def age(self):
		b_data = self.birthday
		b_yr = b_data.year
		b_mo = b_data.month
		b_dy = b_data.day
		birthday = datetime(b_yr, b_mo, b_dy)
		age = int((datetime.now() - birthday).days / 365)
		return age