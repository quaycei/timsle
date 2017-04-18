from django.forms.models import ModelForm
from django import forms

from circle.models import Circle, Link, Project, Content, Guideline

class CircleForm(forms.ModelForm):
	class Meta:
		model = Circle
		exclude = ['creator', 'created_at', 'registry', 'verification',]

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ['creator', 'created_at', 'registry', 'verification',]