from django.forms.models import ModelForm
from django import forms

from circle.models import Circle, Link, Project, Content, Guideline

class CircleStartForm(forms.ModelForm):
	class Meta:
		model = Circle
		exclude = ['group', 'registry', 'rank', 'verification', 'status', 'purpose', 'creator', 'created_at', 'palette', 'icon', 'contact', 'tagline', 'description',]

class CircleForm(forms.ModelForm):
	class Meta:
		model = Circle
		exclude = ['creator', 'created_at', 'registry', 'verification', 'status', 'palette', ]

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ['creator', 'created_at', 'registry', 'verification','status', 'palette',]

class LinkForm(forms.ModelForm):
	class Meta:
		model = Link
		exclude = ['creator', 'created_at', 'registry', 'verification','connection_type', 'name',]
