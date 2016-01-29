from django.http import HttpResponse, Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, forms
from django.shortcuts import render, redirect
from .forms import RegisterForm, InfoForm
from .models import Info
 # inserted this line
#from apps.appname.forms import FormName
#from .models import THE, NAMES, OF, MODELS
def index(request):
  login_form = forms.AuthenticationForm
  register_form = RegisterForm
  users = User.objects.all()
  context = {
    'login_form':login_form(),
    'register_form':register_form(),
    'users':users
  }
  return render(request, 'accounts/index.html',context) # updated this line 

def userprofile(request, id=None):
  info = User.objects.get(id=id)
  info2 = Info.objects.filter(info_user=request.user)
  form = InfoForm()
  form = InfoForm(request.POST)

  context = {
    'form': form,
    'info': info,
    'info2':info2,
  }

  return render(request,'accounts/user.html', context)

def userupdate(request, id=None):
  print " update"
  form = InfoForm(request.POST)
  if form.is_valid:
    print "form is valid"
    form.save(request.user)

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




