from django.http import HttpResponse, Http404
from .models import Distance
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth import login, logout, authenticate, forms
from django.shortcuts import render, redirect # inserted this line
from math import radians, cos, sin, asin, sqrt
#from .models import THE, NAMES, OF, MODELS
def index(request):
	# api key: AIzaSyCXTgg5SPNPtpUnHUySZRJuNmch4hB06w8
	# This block of code was to populate the zipcode database. It should not need to be used again, but keeping it for the moment.
	# zipcodes = open('zipcode.txt')
	# count = 0
	# for line in zipcodes:
	# 	zipcode1, lat1, lon1, = (item.strip() for item in line.split(',', 2))
	# 	lat1 = float(lat1)
	# 	lon1 = float(lon1)
		
	# 	for line in open('zipcode.txt'):
			
	# 		zipcode2, lat2, lon2, = (item.strip() for item in line.split(',', 2))
	# 		if (zipcode1 == zipcode2): 
	# 			break
	# 		lat2 = float(lat2)
	# 		lon2 = float(lon2) 
	# 		distance = haversine(lon1, lat1, lon2, lat2)
	# 		if distance < 10:
	# 			entry = Distance(zipcode1=zipcode1, zipcode2=zipcode2, distance=distance)
	# 			entry.save()
	# 			count += 1
	# 			if count % 1000 == 0:
	# 				print count
	# 				print zipcode1
	context = Distance.objects.filter(zipcode1 = 98101, distance__lte=10)
	
	
 	return render(request, 'zipcodes/index.html', {'context':context}) # updated this line 

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

def contact_form(request):
	form = ContactForm() # We instantiate the ContactForm
	return render(request, 'appname/templatename.html', {'form': form})
def get(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print form.cleaned_data['full_name']
		# you can then do anything you want with the full name
		# you can save it to the database, or store it in session, etc.
		context = {"form": form}
		template = 'wall/contact.html'
		return render(request, template, context)