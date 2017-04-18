from django.forms.models import ModelForm
from django import forms

from registry.models import Registry, Contact



class RegistryForm(forms.ModelForm):
	class Meta:
		model = Registry
		exclude = ['creator', 'created_at', 'verification', 'status','contributors',]


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		exclude = ['creator', 'created_at', 'registry',]