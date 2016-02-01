from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	# url(r'^$', views.index, name='index'),
	url(r'^$', views.EventListView.as_view()),
	url(r'^view/(?P<pk>[-_\w]+)/$', views.EventDetailView.as_view(), name='event-detail'),
	url(r'^create/', views.Create_event.as_view(), name='events-create'),
	url(r'^success/', views.Success.as_view(), name='events-success'),

)
