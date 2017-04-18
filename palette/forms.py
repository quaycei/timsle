from django.forms.models import ModelForm
from django import forms

from palette.models import Palette



class PaletteForm(forms.ModelForm):
	class Meta:
		model = Palette
		exclude = ['creator', 'created_at','registry',]