from django import forms
from django.contrib.auth.models import User
from django.forms.fields import DateField
from .models import Review


class ReviewForm(forms.ModelForm):
	review = forms.TextField(label='Review')
	created_at = forms.DateTimeField(label='Created at')

	class Meta:
		model = Review
		fields = ('review', 'created_at')

	def save(self):
		review = self.cleaned_data['review']
		created_at = self.cleaned_data['created_at']
		

