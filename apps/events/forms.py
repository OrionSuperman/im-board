from django import forms
from .models import Event, Participant
from django.apps import apps
from django.forms import widgets



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
	class Meta:
		model = Event
		fields = (
			'event_name',
			'game', 
			'time',
			'seats',
			'description',
		)
	def save(self):
		event_name = self.cleaned_data['event_name']
		game = apps.get_app_config('games').models['game']
		game = game.filter(game_title = self.cleaned_data['game'])
		time = self.cleaned_data['time']
		seats = self.cleaned_data['seats']
		description = self.cleaned_data['description']
		event=Event.objects.create(event_name=event_name, game=game, time=time, seats=seats,description=description)
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






