from django.shortcuts import render, redirect
from django.contrib.auth import forms
from django.contrib.auth.models import User
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from .models import Review


class Create_Review(View):

	#THIS INFORMATION WILL NEED TO GO IN THE ACCOUNTS VIEWS. ACTUALLY IT WILL BE EASIER TO PUT ALL OF THIS INFORMATION, INCLUDING MODELS AND FORMS IN THE ACCOUNTS APP FOR A HOPEFULLY SEAMLESS TRANSITION.

	#MAKE SURE TO IMPORT REVIEWFORM AND REVIEW MODEL

	#THE GET FUNCTION IS TO RETRIEVE ALL OF THE REVIEWS FOR A GIVEN USER. IT WILL NOT ID. YOU WILL NEED TO GET THE PROFILE USER WITH {{USER.ID}}. IN THE HTML, CREATE A FOR LOOP TO CYCLE THROUGH.

	def get(self):
		review =  Review.objects.all()#add some stuff here, can also user filter to reduce time and space and privacy if people care about that
		review_form = ReviewForm()
		context={
			'review_form':review_form,
		}
		return render(request, '')
		#put this in the acccounts view ,and render the user html page

	def post(self, request):
		form = ReviewForm(request.POST)
		if form.is_valid():
			form.save(request.user)	

			return redirect('/user/{}'.format(profile_id))

		return redirect('/user/{}'.format(profile_id))
def index(request):
	reviews = Reviews.objects.filter()


