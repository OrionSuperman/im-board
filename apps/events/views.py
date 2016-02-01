from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic import View
from django.contrib.auth import forms
from .forms import EventForm
from django.apps import apps
from math import radians, cos, sin, asin, sqrt
from .models import Distance, Location, Participant, Event
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
import random
from django.utils import timezone
Game = apps.get_app_config('games').models['game']



class EventListView(ListView):
	model = Event
	template_name = 'events/list.html'
	def get_context_data(self, **kwargs):
		context = super(EventListView, self).get_context_data(**kwargs)
		return context

class EventDetailView(DetailView):
	model = Event
	template_name = 'events/detail.html'
	def get_context_data(self, **kwargs):
		context = super(EventDetailView, self).get_context_data(**kwargs)
		return context

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
			print '*' * 100
			print request.session.items()
			user_obj = User.objects.get(id=request.session['user_id'])

			event = form.save(user_obj)

			return redirect('/events/view/' + str(event.id))
		else:
			context = {
				'form': form,
			}
			return render(request, 'events/create.html', context)

class Success(View):
	def get(self, request):
		return render(request, 'events/success.html')
		

def events_near_zip(request, zipcode = 98003, distance = 25):
  zips = Distance.objects.all().filter(zipcode1 = zipcode, distance__lte = distance)
  alist = []
  distances = {}
  
  for each in zips:
    alist.append(each.zipcode2)
    if not each.zipcode2 in distances:
    	distances[each.zipcode2] = each.distance

  events = Event.objects.all().filter(location__zipcode__in = alist)



  return render(request, 'events/nearby.html', {'events':events, 'distances':distances})

def event_search(request):
	zipcode = request.POST['zipcode']
	distance = request.POST['distance']
	return redirect('/events/nearby/' + str(zipcode) + '/' + str(distance))


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


###############################################
# the next two functions are used to initially populate the zipcode distances database. This will have to be done again when this is deployed.
###############################################
# def index(request):
# 	# api key: AIzaSyCXTgg5SPNPtpUnHUySZRJuNmch4hB06w8
# 	# This block of code was to populate the zipcode database. It should not need to be used again, but keeping it for the moment.
# 	zipcodes = open('zipcode.txt')
# 	count = 0
# 	for line in zipcodes:
# 		zipcode1, lat1, lon1, = (item.strip() for item in line.split(',', 2))
# 		lat1 = float(lat1)
# 		lon1 = float(lon1)
		
# 		for line in open('zipcode.txt'):
			
# 			zipcode2, lat2, lon2, = (item.strip() for item in line.split(',', 2))
# 			if (zipcode1 == zipcode2): 
# 				break
# 			lat2 = float(lat2)
# 			lon2 = float(lon2) 
# 			distance = haversine(lon1, lat1, lon2, lat2)
# 			if distance < 25:
# 				entry = Distance(zipcode1=zipcode1, zipcode2=zipcode2, distance=distance)
# 				entry.save()
# 				count += 1
# 				if count % 1000 == 0:
# 					print count
# 					print zipcode1

# 	print "THE DATABASE HAS BEEN BUILT. ALL YE REJOICE"
# 	context = Distance.objects.filter(zipcode1 = 98101, distance__lte=10)
	
	
#  	return render(request, 'events/index.html', {'context':context}) # updated this line 
# def haversine(lon1, lat1, lon2, lat2):
#     """
#     Calculate the great circle distance between two points 
#     on the earth (specified in decimal degrees)
#     """
#     # convert decimal degrees to radians 

#     lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
#     # haversine formula 

#     dlon = lon2 - lon1 
#     dlat = lat2 - lat1 

#     a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
#     c = 2 * asin(sqrt(a)) 
#     km = 6367 * c
#     miles = km / 1.60934
#     return miles

#################################################
# Populating events to test searching code below
#################################################

# def index(request):
# 	#populating the events field

# 	zipcodes = open('zipcode.txt')
# 	count = 0
# 	for line in zipcodes:
# 		for i in range(3):
# 			zipcode1, lat1, lon1, = (item.strip() for item in line.split(',', 2))

# 			WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone", "fun", "Party", "games", "event", "friends", "thinking", "free", "horse")
# 			event_name = ''
# 			for i in range(3):
# 				event_name += random.choice(WORDS) + ' '

# 			time = timezone.now()

# 			seats = random.randint(2,8)

# 			description = ''
# 			for i in range(5):
# 				description += random.choice(WORDS) + ' '

# 			user_obj = User.objects.get(id=3)

# 			event=Event.objects.create(event_name=event_name, time=time, seats=seats,description=description, seats_filled = 0, host=user_obj)

# 			# Adding each game selected to the event.
# 			game_obj = Game.objects.get(game_title="Dominion")
# 			event.games.add(game_obj)

# 			street1 = '123 Main Street'
# 			street2 = 'Apt 21'
# 			city = 'Nearby'
# 			state = 'EX'
# 			zipcode = zipcode1

# 			location = Location.objects.create(event=event, street1=street1, street2=street2, city=city, state=state, zipcode=zipcode )
# 		count +=1
# 		if count % 1000 == 0:
# 			print zipcode1
# 	print "EVENTS HAVE BEEN PLACED"