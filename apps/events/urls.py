from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	# url(r'^$', views.index, name='index'),
	url(r'^$', views.events_near_zip),
	url(r'^search/$', views.event_search),
	url(r'^nearby/(?P<zipcode>\d+)/(?P<distance>\d+)?', views.events_near_zip),
	url(r'^nearby/(?P<zipcode>\d+)?', views.events_near_zip),
	url(r'^view/(?P<pk>[-_\w]+)/$', views.EventDetailView.as_view(), name='event-detail'),
	url(r'^create/', views.Create_event.as_view(), name='events-create'),
	url(r'^success/', views.Success.as_view(), name='events-success'),

)
