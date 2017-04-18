from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_slug
from django.contrib.contenttypes.fields import GenericRelation






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

class Registry(models.Model):
    creator = models.ForeignKey(User, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    verification = models.IntegerField(choices=VERIFICATION, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    name = models.CharField(max_length=50)
    mission = models.TextField(max_length=250, default=None)

    
    def __str__(self):
        return self.name 

class Contact(models.Model):
    registry = models.ForeignKey(Registry, default=None)
    first_name = models.CharField(max_length=140, default=None)
    last_name = models.CharField(max_length=140, default=None)
    office = models.CharField(max_length=140, default=None, blank=True, null=True)
    address_line_1 = models.CharField(max_length=140, default=None, blank=True, null=True)
    address_line_2 = models.CharField(max_length=140, default=None, blank=True, null=True)
    city = models.CharField(max_length=140, default=None, blank=True, null=True)
    state_province_region = models.CharField(max_length=140, default=None, blank=True, null=True)
    zip_postal_code = models.CharField(max_length=140, default=None, blank=True, null=True)
    country = models.CharField(max_length=140, default=None, blank=True, null=True)
    website = models.CharField(max_length=140, default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=140, default=None, blank=True, null=True)
    email_address = models.CharField(max_length=140, default=None)
    contact_note = models.TextField(max_length=300, default=None, blank=True, null=True)
    creator = models.ForeignKey(User, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return self.registry.name + " : " + self.first_name + " " + self.last_name


