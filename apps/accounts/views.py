from django.http import HttpResponse, Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, forms
from django.shortcuts import render, redirect
from .forms import RegisterForm, InfoForm, ReviewForm
from .models import Info, Review, Address
from django.apps import apps
Event = apps.get_app_config('events').models['event']
Distance = apps.get_app_config('events').models['distance']

 # inserted this line
#from apps.appname.forms import FormName
#from .models import THE, NAMES, OF, MODELS
def index(request):
  review_form = ReviewForm()
  # info_obj = Info.objects.get(info_user = request.user)
  # review = Review.objects.filter(review_for = info_obj)
  #this first fetch is to get all, and in html, we can filter through an if statement. The second fetch uses filtering.

  login_form = forms.AuthenticationForm
  register_form = RegisterForm
  users = User.objects.all()
  context = {
  'login_form':login_form(),
  'register_form':register_form(),
  'users':users,
  # 'review':review,
  # 'review_form':review_form,
  }
 
  return render(request, 'accounts/index.html',context) # updated this line 


def createreview(request, for_id):

  if not (int(for_id) == int(request.session['user_id'])):
    # profile_page will be a hidden variable in the review form with a value of {{user.id}}
    userpage = User.objects.get(id=for_id) 

    review = Review.objects.create(
        review_for = Info.objects.get(info_user = User.objects.get(id = for_id)),
        review=request.POST['review'], 
        rating=request.POST['rating'], 
        review_by=Info.objects.get(info_user = User.objects.get(id=request.session['user_id']))
        )
    return redirect('/user/'+ for_id)
  else:
    messages.error(request, "Invalid")
    return redirect('/user/'+ for_id)

def userprofile(request, id=None):
    user = User.objects.get(id=id)
    form = InfoForm()
    review_form = ReviewForm()

    user_obj = User.objects.get(id=id)
    info_obj = Info.objects.get(info_user = user_obj)
    reviews = Review.objects.filter(review_for = info_obj)
    events = get_events_nearby(info_obj.get_user_zipcode())


    context = {
    'form': form,
    'user': user,
    'review_form':review_form,
    'reviews' : reviews,
    'events' : events,
    }

    return render(request,'accounts/user.html', context)

def get_events_nearby(zipcode):
  zips = Distance.objects.all().filter(zipcode1 = 98003, distance__lte = 10)
  alist = []
  for each in zips:
    alist.append(each.zipcode2)
  events = Event.objects.all().filter(location__zipcode__in = alist)

  return events

def userupdate(request, id=None):
  print " update"
  form = InfoForm(request.POST)
  if form.is_valid():
    print "form is valid"

    user_obj = User.objects.get(id=id)

    form.save(user_obj)

  # obj = form.save(commit=False)
  # obj.user = request.user
  # obj.save()



  print "not valid"
  return redirect ('/user/{}'.format(id))

class Login(View):
  form = forms.AuthenticationForm
  def get(self, request):
    context = {'form': self.form()}
    return render(request, 'accounts/index.html', context)
  def post(self, request):
    form = self.form(None, request.POST)
    context = {'form':form}
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        user2 = User.objects.get(username=username)
        request.session['user_id'] = user2.id
        # messages.success(request, "Successfully logged in")
        return redirect('/')
      else:
          messages.error(request, "Invalid")
          return redirect('/')
    else:
        # login_form = forms.AuthenticationForm
        # register_form = forms.UserCreationForm
        # context = {
        #   'login_form':login_form(),
        #   'register_form':register_form(),
        # }
        messages.error(request, "Invalid Login")
        return redirect('/')

class Logout(View):
  def get(self, request):
    logout(request)
    return redirect('/')

class Register(View):

  form = RegisterForm
  def get(self, request):
    context = {'form': self.form()}
    return render(request, 'accounts/index.html', context)
  def post(self, request):
    form = self.form(request.POST)
    print '*' * 100
    print form.is_valid()
    if form.is_valid():
      username = form.cleaned_data['username']
      form.save()
      user2 = User.objects.get(username=username)
      request.session['user_id'] = user2.id
      # messages.success(request, "Successfully Registered")
      return redirect('/')

    else:
      messages.error(request, form.errors)
      return redirect('/')


class Success(View):
    def get(self, request):
      return render(request, 'accounts/success.html')