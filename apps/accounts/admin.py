from django.contrib import admin
from .models import User, Info

class UserAdmin(admin.ModelAdmin):
	class Meta:
		model = User

admin.site.register(Info)

# Register your models here.
