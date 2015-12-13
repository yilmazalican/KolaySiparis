from __future__ import unicode_literals
from datetime import datetime
from django.db import models

from django.contrib.auth.models import User




class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_adress = models.CharField(max_length=1000)


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    phone = models.BigIntegerField()



class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    joindate = models.DateTimeField(default=datetime.now, blank=True)
    delivertime = models.CharField(max_length=100)
    district = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default = True)


class Restaurant_Promos(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Menu(models.Model):
    name  = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)




class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField()
    status = models.BooleanField()
    menu = models.ManyToManyField(Menu)
    totalprice = models.IntegerField(default=0)
    seen = models.BooleanField(default=False)
