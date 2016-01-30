from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
	url(r'^create/?$', views.Create_Review.as_view(), name = 'create_review'),
]