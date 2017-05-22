from __future__ import unicode_literals
from django.db import models
from ordered_model.models import OrderedModel
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from palette.models import Palette, Element


from registry.models import Registry, Contact

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


CONNECTION_TYPES = (
        (0, 'Internal'),
        (1, 'External'),
    )

RANK_TYPES = (
        (0, 'Torus'),
        (1, 'Station'),
        (2, 'Probe'),
        (3, 'Lander'),
        (4, 'Mothership'),
    )


PURPOSE = (
        (0, 'None'),
        (1, 'Add Registry'),
        (2, 'Add Offering'),
        (3, 'Add User'),
        (4, 'Add Filter'),
    )

GROUP = (
        (0, 'User'),
        (1, 'Offering'),
        (2, 'Need'),
        (3, 'Filter'),
    )


class Tag(models.Model):
    name = models.CharField(max_length=50)
    related_tag = models.ManyToManyField('self', blank=True, default=None)

    def __str__(self):
        return self.name 


class Circle(OrderedModel):
    group = models.IntegerField(choices=GROUP,null=True, blank=True, default=0)
    registry = models.ForeignKey(Registry, default=None)
    rank = models.IntegerField(choices=RANK_TYPES,default=0)
    verification = models.IntegerField(choices=VERIFICATION,default=0)
    status = models.IntegerField(choices=STATUS,default=0)
    purpose = models.IntegerField(choices=PURPOSE,default=0, blank=True, null=True)
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    palette = models.ForeignKey(Palette, default=None, blank=True, null=True)
    icon = models.ForeignKey(Element, null=True, blank=True, default=None)
    contact = models.ForeignKey(Contact, null=True, blank=True, default=None)
    name = models.CharField(max_length=50)
    tagline = models.CharField(max_length=140, default=None, blank=True, null=True)
    description = models.TextField(max_length=140, null=True, default=None, blank=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.name 


class Link(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    registry = models.ForeignKey(Registry, default=None)
    circle = models.ForeignKey(Circle, default=None, blank=True, null=True)
    connection_type = models.IntegerField(choices=CONNECTION_TYPES,default=0)
    verification = models.IntegerField(choices=VERIFICATION,default=1)
    name = models.CharField(max_length=21, default=None, blank=True, null=True)
    options = models.ManyToManyField('Circle', related_name='parents', default=None, blank=True)
    directional_question = models.CharField(max_length=140, null=True, default="What would you like to do?", blank=True,)


class Project(models.Model):
    registry = models.ForeignKey(Registry, default=None)
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
    registry = models.ForeignKey(Registry, default=None)
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
        (4, 'Buy'),
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
    registry = models.ForeignKey(Registry, default=None, blank=True, null=True)
    purpose = models.IntegerField(choices=PURPOSE,default=0)
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

    def __str__(self):
        return self.text


