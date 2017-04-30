from django.forms.models import ModelForm
from django import forms

from palette.models import Palette



class PaletteStartForm(forms.ModelForm):
	class Meta:
		model = Palette
		exclude = ['creator', 'created_at', 'name','element',]


class PaletteForm(forms.ModelForm):
	class Meta:
		model = Palette
		exclude = ['creator', 'created_at', 'name',]