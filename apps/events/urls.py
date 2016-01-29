from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
  url(r'^create/', views.Create_event.as_view(), name='events-create'),
  url(r'^success/', views.Success.as_view(), name='events-success'),

)
