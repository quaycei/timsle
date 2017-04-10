from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from allauth.account.models import EmailAddress

from circle.models import Circle, Project, Content, Guideline

class Pact(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Completed'),
        (3, 'Archived'),
    )
    
    owner = models.ForeignKey(User, blank=False)  
    content = models.ForeignKey(Content, blank=False)
    answer = models.CharField(max_length=200, blank=False)
    goal = models.IntegerField(blank=True, default=5)
    motivation = models.TextField(default=None) 
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.answer
    
    def approved_buddies(self):
        return self.buddy_set.filter(status=2)
    
    def is_approved_buddy(self, user):
        for buddy in self.approved_buddies():
            if buddy.user == user:
                return True
        
        return False
    
    def get_checkin_count(self):
        return self.checkin_set.all().count()

    def get_all_checkins(self):
        return checkin_set.all()


    
class Checkin(models.Model):
    pact = models.ForeignKey(Pact, blank=False)
    submitted_by = models.ForeignKey(User, blank=False)
    text = models.CharField(blank=True, max_length=140)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    

class Buddy(models.Model):
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Yes'),
        (3, 'No'),
        (4, 'Ignore Request'),
    )  
    
    pact = models.ForeignKey(Pact, blank=False)
    user = models.ForeignKey(User, blank=True, null=True, default=None)
    email = models.CharField(max_length=200, blank=True) 
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def save(self, *args, **kwargs):
        if self.user:
            email = self.user.email
            self.email = email
        elif self.email:
            email = self.email
            try:
                email = EmailAddress.objects.get(email=email)
                self.user = email.user
            except Exception:
                pass
                
        super(Buddy, self).save(*args, **kwargs)
