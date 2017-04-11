from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_slug
from django.contrib.contenttypes.fields import GenericRelation
from palette.models import Palette, Element

STATUS = (
        (0, 'Pending'),
        (1, 'Online'),
        (2, 'Offline'),
        (3, 'Removed'),
    )

VERIFICATION = (
        (0, 'Pending'),
        (1, 'Verified'),
        (2, 'Flagged'),
        (3, 'Declined'),
    )

RANK_TYPES = (
        (0, 'Torus'),
        (1, 'Station'),
        (2, 'Probe'),
        (3, 'Lander'),
        (4, 'Mothership'),

    )

class Contact(models.Model):
    contact_name = models.CharField(max_length=140, default=None, blank=True)
    website = models.CharField(max_length=140, default=None, blank=True)
    phone_number = models.CharField(max_length=140, default=None, blank=True)
    email_address = models.CharField(max_length=140, default=None, blank=True)
    contact_note = models.TextField(max_length=300, default=None, blank=True)

    def __str__(self):
        return self.contact_name


class Circle(models.Model):
    rank = models.IntegerField(choices=RANK_TYPES,default=0)
    verification = models.IntegerField(choices=VERIFICATION,default=0)
    status = models.IntegerField(choices=STATUS,default=0)
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    palette = models.ForeignKey(Palette, default=None, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, default=None)
    slug = models.CharField(max_length=21, null=True, blank=True, unique=True, validators=[validate_slug])
    name = models.CharField(max_length=50)
    icon = models.ForeignKey(Element, null=True, blank=True, default=None)
    contact = models.ForeignKey(Contact, null=True, blank=True, default=None)
    tagline = models.CharField(max_length=140, default=None, blank=True)
    description = models.TextField(max_length=140, default=None, blank=True)
    directional_question = models.CharField(max_length=140, null=True, default="What would you like to do?", blank=True,)


    def __str__(self):
        return self.name 


class Project(models.Model):
    status = models.IntegerField(
        choices=STATUS,
        default=0,
    )
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    palette = models.ForeignKey(Palette, default=None, blank=True, null=True)
    name = models.CharField(max_length=60)
    icon = models.ForeignKey(Element, null=True, blank=True, default=None)
    tagline = models.CharField(max_length=140, default=None, blank=True)
    description = models.TextField(max_length=140, default=None, blank=True)
    circle = models.ManyToManyField(Circle, default=None, blank=True)



    def __str__(self):
        return self.name


class Content(models.Model):
    status = models.IntegerField(
        choices=STATUS,
        default=0,
    )
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
    palette = models.ForeignKey(Palette, default=None, blank=True, null=True)
    name = models.CharField(max_length=60)
    icon = models.ForeignKey(Element, null=True, blank=True, default=None)
    tagline = models.CharField(max_length=140, default=None, blank=False)
    description = models.TextField(max_length=140, default=None, blank=False)
    question = models.TextField(max_length=140, default=None, blank=False)
    project = models.ForeignKey(Project, default=None, blank=False)


    def __str__(self):
        return self.name


class Guideline(models.Model):
    rank = models.IntegerField(choices=RANK_TYPES,default=3)
    status = models.IntegerField(
        choices=STATUS,
        default=0,
    )
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


