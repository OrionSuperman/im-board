from django.conf.urls import patterns, url
from . import views
#from .views import NamesOfViewClassesForDetailAndListView
urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^register/$', views.Register.as_view(), name='accounts-register'),
  url(r'^success/$', views.Success.as_view(), name='accounts-success'),
  url(r'^login/$', views.Login.as_view(), name='accounts-login'),  
)