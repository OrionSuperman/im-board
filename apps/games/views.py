from django.http import HttpResponse, Http404
from .forms import ContactForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth import login, logout, authenticate, forms
from django.shortcuts import render, redirect # inserted this line
#from .models import THE, NAMES, OF, MODELS
def index(request):
  return render(request, 'games/index.html') # updated this line 
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