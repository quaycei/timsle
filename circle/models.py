from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_slug

class Style(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=30)
    color_dark = models.CharField(max_length=7)
    color_light = models.CharField(max_length=7)
    accent_color_dark = models.CharField(max_length=7)
    accent_color_light = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Group(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=30)
    tagline = models.CharField(max_length=140)
    description = models.TextField(max_length=140)
    style = models.ForeignKey(Style, default=None, blank=True)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])

    def __str__(self):
        return self.name

class Organization(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=30)
    tagline = models.CharField(max_length=140)
    description = models.TextField(max_length=140)
    style = models.ForeignKey(Style, default=None, blank=True)
    group = models.ForeignKey(Group, default=None, blank=True)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])

    def __str__(self):
        return self.name

class Circle(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=30)
    tagline = models.CharField(max_length=140)
    description = models.TextField(max_length=140)
    group = models.ForeignKey(Group, default=None, blank=True)
    organization = models.ForeignKey(Organization, default=None, blank=True)
    style = models.ForeignKey(Style, default=None, blank=True)
    slug = models.CharField(max_length=21, blank=False, unique=True, validators=[validate_slug])

    def __str__(self):
        return self.name

class Project(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=30)
    tagline = models.CharField(max_length=140)
    description = models.TextField(max_length=140)
    circle = models.ForeignKey(Circle, default=None)
    group = models.ForeignKey(Group, default=None, blank=True)
    style = models.ForeignKey(Style, default=None, blank=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    TYPE_OF_CONTENT_CHOICES = (
        (0, 'Text'),
        (1, 'Challenge'),
        (2, 'Photo'),
        (3, 'Video'),
    )
    type_of_circle = models.IntegerField(
        choices=TYPE_OF_CONTENT_CHOICES,
        default=0,
    )
    name = models.CharField(max_length=60)
    tagline = models.CharField(max_length=140)
    description = models.TextField(max_length=140)
    question = models.TextField(max_length=140, default=None, blank=False)
    project = models.ForeignKey(Project, default=None, blank=False)
    style = models.ForeignKey(Style, default=None, blank=True)

    def __str__(self):
        return self.name


class Guideline(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    TYPE_OF_GUIDELINE_CHOICES = (
        (0, 'Example'),
        (1, 'Rule'),
    )
    type_of_guideline = models.IntegerField(
        choices=TYPE_OF_GUIDELINE_CHOICES,
        default=0,
    )
    text = models.CharField(max_length=300)
    content = models.ForeignKey(Content, default=None, blank=False)

    def __str__(self):
        return self.text


