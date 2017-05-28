from django.forms.models import ModelForm
from django import forms

from registry.models import Registry, Contact


class RegistryStartForm(forms.ModelForm):
	class Meta:
		model = Registry
		exclude = ['creator', 'created_at', 'verification', 'status', 'mission', 'mission_why', 'palette', 'theme_color']



class RegistryForm(forms.ModelForm):
	class Meta:
		model = Registry
		exclude = ['creator', 'created_at', 'verification', 'status',]


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		exclude = ['creator', 'created_at', 'registry',]