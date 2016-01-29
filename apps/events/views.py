from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic import View
from django.contrib.auth import forms
from .forms import EventForm
from django.apps import apps




class Create_event(View):
	form = EventForm
	def get(self, request):
		context = {
			'form': self.form(),
		}
		return render(request, 'events/create.html', context)


	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			form.save()

			return render(request, 'events/event_created.html', {'context':form})
		else:
			context = {
				'form': form,
			}
			return render(request, 'events/create.html', context)

class Success(View):
	def get(self, request):
		return render(request, 'events/success.html')
		


# class Participant_Entry(View):
# 	if request.method == 'POST':
# 		form = ParticipantForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponse('adslkf')
# 		else:
# 			return HttpResponse('askdf')
# 	else:
# 		return HttpResponse('a;lksdfj')
