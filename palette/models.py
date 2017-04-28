from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_slug
from colorful.fields import RGBColorField

from registry.models import Registry


class Element(models.Model):
    ELEMENT_TYPES = (
        (0, 'Icon'),
        (1, 'Width'),
        (2, 'CSS Property'),
        (3, 'Theme'),
    )
    element_type = models.IntegerField(choices=ELEMENT_TYPES,default=0)
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Palette(models.Model):
    creator = models.ForeignKey(User, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=50)
    background_color = RGBColorField()
    foreground_color = RGBColorField()
    accent_color_dark = RGBColorField()
    accent_color_light = RGBColorField()
    element = models.ManyToManyField(Element, blank=True, default=None)

    def __str__(self):
        return self.name


