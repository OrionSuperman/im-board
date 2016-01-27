from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')
	email = forms.EmailField(label='Email Address')
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
			return user