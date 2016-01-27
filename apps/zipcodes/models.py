from __future__ import unicode_literals

from django.db import models

class Distance(models.Model):
	zipcode1 = models.IntegerField()
	zipcode2 = models.IntegerField()
	distance = models.FloatField()
	def __str__(self):
		return self.zipcode1
	class Meta:
		db_table = 'distances'
