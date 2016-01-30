from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib.auth.models import User

class Review(models.Model):


	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	review = models.TextField()
	rating = models.CharField(max_length=1)
	#still need to add more for the rating field for 1-5.

	review_by = models.ForeignKey(User)
	review_for = models.ForeignKey(User)
	# rating = models. add later...
	class Meta:
		db_table = 'reviews'

