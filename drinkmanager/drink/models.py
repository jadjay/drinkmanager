from __future__ import unicode_literals

from django.db import models
from django.core.files import File

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
from jsonfield import JSONField
import urllib2
#import simplejson
import cStringIO

class Drink(models.Model):
    def __str__(self):
        return "%s" % self.name

    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='static/uploads/',default="static/uploads/canette.jpg")
    description = JSONField(null=True,blank=True,)
    def lastStock(self):
        if not self.stock_set.all():
            return None
        return self.stock_set.latest('date')

class Stock(models.Model):
    def __str__(self):
        return "%s %s %s" % (self.date.strftime("%F"),self.drink.name,self.quantity)

    date = models.DateField()
    quantity = models.IntegerField()
    drink = models.ForeignKey(Drink)

class Consumption(models.Model):
    def __str__(self):
        return "%s %s %s" % (self.date.strftime("%F|%H:%M:%S"),self.user.username,self.drink.name)

    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink)
    def getuser(self):
        return self.user
