from django.http import HttpResponse, Http404
from .forms import ContactForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth import login, logout, authenticate, forms
from django.shortcuts import render, redirect # inserted this line
from .models import Game, GameType
def index(request):
  return render(request, 'games/index.html') # updated this line 

class GameListView(ListView):
	model = Game
	template_name = 'games/list.html'
	def get_context_data(self, **kwargs):
		context = super(GameListView, self).get_context_data(**kwargs)
		return context

# class GameDetailView(DetailView):
# 	