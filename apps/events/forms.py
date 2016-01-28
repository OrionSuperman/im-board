from django import forms
from .models import Event, Participant

class EventForm(forms.Form):
	event_name = forms.CharField(label='Event Name', max_length=50)	
	game = forms.CharField(label='Game', max_length=50)
	time = forms.DateTimeField(label='Time and Date')
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
		game = self.cleaned_data['game']
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






