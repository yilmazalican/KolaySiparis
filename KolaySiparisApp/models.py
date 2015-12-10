from __future__ import unicode_literals
from datetime import datetime
from django.db import models

from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User)
    phone = models.BigIntegerField()
    adress = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    joindate = models.DateTimeField(default=datetime.now, blank=True)
    delivertime = models.CharField(max_length=100)
    status = models.BooleanField(default = True)


class Restaurant_Promos(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name  = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=100)



class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    time = models.DateTimeField()
    status = models.BooleanField()
    menu = models.ManyToManyField(Menu)
    totalprice = models.IntegerField(default=0)

class Customer_Orders(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order)
