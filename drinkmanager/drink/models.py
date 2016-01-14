from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
from jsonfield import JSONField

#class Customer(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    
class Drink(models.Model):
    def __str__(self):
        return "%s" % self.name

    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='static/uploads/',default="uploads/canette_coca.jpeg")
    description = JSONField(null=True,blank=True,)
#default="{}")
    def lastStock(self):
        if self.stock_set.all().exists():
            return self.stock_set.latest('date')
        else:
            return None

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
