from django.conf.urls import patterns, url
from . import views
#from .views import NamesOfViewClassesForDetailAndListView
urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
)