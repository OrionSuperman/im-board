from django import forms
from django.forms import ModelForm
class ContactForm(forms.Form):
  full_name = forms.CharField(label='Your full name', max_length=100)