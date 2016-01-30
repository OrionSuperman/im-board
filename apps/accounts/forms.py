from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Info, Address, Review, User_Profile_Review
from django.forms import widgets
from django.apps import apps



Game = apps.get_app_config('games').models['game']
# Zipcode = apps.get_app_config('zipcodes').models['distance']
GameType = apps.get_app_config('games').models['gametype']
# Event = apps.get_app_config('events').models['event']


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
	game = forms.ModelMultipleChoiceField(queryset=Game.objects.all(), label='Games')
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
	def save(self,user_obj):

		

		bio = self.cleaned_data['bio']
		city = self.cleaned_data['city']
		games = self.cleaned_data['game']

		# This creates the user object that we are working with. The +1 is needed, don't remove. For some reason the number pulled is 1 lower than needed, and that was the issue we were experiencing.
		# print '*' * 100
		# print user_obj
		# user_obj = User.objects.get(id=user_obj.id)
		user_int = int(user_obj.id)

		# Use this section to update the **Info** information
		print '*' * 100
		print user_obj
		info_obj = Info.objects.get(info_user = User.objects.get(id=22))
		info_obj.bio=bio
		
		info_obj.save()

		# Use this section to update the **Game** information
		info_obj.games.clear()
		for game in games:
			game_obj = Game.objects.get(game_title=game.game_title)
			info_obj.games.add(game_obj)
			# info_obj.games=game_obj
			# print info_obj.game
			# info_obj.save()

		# Use this section to update the **Address** information
		address_obj = info_obj.address
		address_obj.city = city
		address_obj.save()


		# info.games=games
		return info_obj


class ReviewForm(forms.ModelForm):
	review = forms.CharField(label='Review')
	created_at = forms.DateTimeField(label='Created at')

	class Meta:
		model = User_Profile_Review
		fields = ['review', 'created_at']




