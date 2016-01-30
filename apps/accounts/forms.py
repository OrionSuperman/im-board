from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Info, Address
from django.forms import widgets
from django.apps import apps





class RegisterForm(UserCreationForm):
	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')
	email = forms.EmailField(label='Email Address')
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
			return user


class InfoForm(forms.Form):

	# def __init__(self, *kargs, **kwargs):
	# 	instance =kwargs.get('instance', None)

	# 	kwargs.update(initial={
	# 		'bio':
	# 		})

	bio = forms.CharField(label='Bio', required=False)
	city = forms.CharField(label='City', required=False)
	# games = forms.CharField(label='Games', required=False)
	class Meta:
		model = Info
		fields = (
			'bio', 
			'city', 
			# 'games'
			)
		# fields = {
		# 	'bio':

		# }
	def save(self,user_id):

		


		bio = self.cleaned_data['bio']
		city = self.cleaned_data['city']
		# games = self.cleaned_data['games']
		user_obj = User.objects.get(id=user_id.id)
		print '*' * 50
		print user_obj.id
		user_int = int(user_obj.id) + 1
		#This works to update the Info information.
		info_obj = Info.objects.get(info_user = user_int)
		info_obj.bio=bio
		info_obj.save()

		# This works to update the Address information
		address_obj = info_obj.address
		address_obj.city = city
		address_obj.save()


		# info.games=games
		return info_obj





