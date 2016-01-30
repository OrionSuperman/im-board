from django.http import HttpResponse, Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, forms
from django.shortcuts import render, redirect
from .forms import RegisterForm, InfoForm, ReviewForm
from .models import Info, Review, User_Profile_Review


 # inserted this line
#from apps.appname.forms import FormName
#from .models import THE, NAMES, OF, MODELS
def index(request):
  review_form = ReviewForm()
  review =  User_Profile_Review.objects.all()
  review = Review.objects.filter(user_id = request.user.id)
  #this first fetch is to get all, and in html, we can filter through an if statement. The second fetch uses filtering.

  login_form = forms.AuthenticationForm
  register_form = RegisterForm
  users = User.objects.all()
  context = {
    'login_form':login_form(),
    'register_form':register_form(),
    'users':users,
    'review':review,
    'review_form':review_form,
  }
  return render(request, 'accounts/index.html',context) # updated this line 


def createreview(self, request):
  # profile_page will be a hidden variable in the review form with a value of {{user.id}}
  userpage = User.objects.get(id=request.POST['profile_page']) 
      
  review = User_Profile_Review.objects.create(user_id=userpage, created_at=request.POST['created_at'], updated_at=request.POST['updated_at'], review=request.POST['review'], rating=request.POST['rating'], review_by=request.user)
  

def userprofile(request, id=None):
  user = User.objects.get(id=id)
  form = InfoForm()
  # form = InfoForm(request.POST)

  context = {
    'form': form,
    'user': user,
    # 'info2':info2,
  }

  return render(request,'accounts/user.html', context)

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
    if form.is_valid():
      username = form.cleaned_data['username']
      form.save()
      user2 = User.objects.get(username=username)
      request.session['user_id'] = user2.id
      # messages.success(request, "Successfully Registered")
      return redirect('/')
    else:
      messages.error(request, "Invalid Registration")
      return redirect('/')


class Success(View):
  def get(self, request):
    return render(request, 'accounts/success.html')




