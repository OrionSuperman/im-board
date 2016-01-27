from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^', include('apps.accounts.urls')), # we inserted this line!!!
	url(r'^accounts/', include('apps.accounts.urls')),
	url(r'^zipcodes/', include('apps.zipcodes.urls')),
	url(r'admin/', include(admin.site.urls)),
)