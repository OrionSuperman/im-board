from django import forms
from .models import Event, Participant, Location
from django.apps import apps
from django.forms import widgets
from datetime import datetime
Game = apps.get_app_config('games').models['game']

class CustomDateInput(widgets.TextInput):
    input_type = 'date'

class CustomTimeInput(widgets.TextInput):
    input_type = 'time'

class EventForm(forms.Form):
	
	gameob = apps.get_app_config('games').models['game']
	

	event_name = forms.CharField(label='Event Name', max_length=50)	
	game = forms.ModelMultipleChoiceField(queryset=gameob.objects.all(), label='Games')
	date = forms.DateField(label='Date', widget=CustomDateInput)
	time = forms.TimeField(widget=CustomTimeInput, label='Time')
	seats = forms.IntegerField(label='Number of seats available')
	description = forms.CharField(label='Description')
	street1 = forms.CharField(label='Address')
	street2 = forms.CharField(label='Apt/Suite', required=False)
	city = forms.CharField(label='City')
	state = forms.CharField(label='State')
	zipcode = forms.IntegerField(label='Zipcode')

	class Meta:
		model = Event
		fields = (
			'event_name',
			'game', 
			'time',
			'seats',
			'description',
			'street1', 
			'street2', 
			'city',
			'state',
			'zipcode',
		)
	def save(self, user_obj):
		event_name = self.cleaned_data['event_name']
		date = self.cleaned_data['date']
		time = datetime.combine(date, self.cleaned_data['time'])
		seats = self.cleaned_data['seats']
		description = self.cleaned_data['description']
		event=Event.objects.create(event_name=event_name, time=time, seats=seats,description=description, seats_filled = 0, host=user_obj)

		# Adding each game selected to the event.
		games = self.cleaned_data['game']
		for game in games:
			game_obj = Game.objects.get(game_title=game.game_title)
			event.games.add(game_obj)

		street1 = self.cleaned_data['street1']
		street2 = self.cleaned_data['street2']
		city = self.cleaned_data['city']
		state = self.cleaned_data['state']
		zipcode = self.cleaned_data['zipcode']

		location = Location.objects.create(event=event, street1=street1, street2=street2, city=city, state=state, zipcode=zipcode )

		return event



	# class ParticipantForm(forms.ModelForm):
	# 	class Meta:
	# 		model = Participant
	# 		fields = [
	# 			'first_name',
	# 			'contact',
	# 			'bio',
	# 		]
	# 	def save(self):
	# 		first_name = self.cleaned_data['first_name']
	# 		contact = self.cleaned_data['contact']
	# 		bio = self.cleaned_data['bio']
	# 		Participant.save()






