from __future__ import unicode_literals
from django.db import models


class Line(models.Model):
    height = models.IntegerField(default=20)
    drop = models.IntegerField(default=20)
    
    
