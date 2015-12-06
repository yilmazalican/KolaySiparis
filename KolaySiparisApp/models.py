from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User)
    phone = models.BigIntegerField()
    adress = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    
