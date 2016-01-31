from django.contrib import admin
from .models import User, Info, Address, Review

class UserAdmin(admin.ModelAdmin):
	class Meta:
		model = User
admin.site.register(Review)
admin.site.register(Info)
admin.site.register(Address)
# Register your models here.
