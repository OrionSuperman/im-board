
from django.contrib import admin

# Register your models here.
from .models import Event
from .models import Participant
from .models import Location
admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Location)