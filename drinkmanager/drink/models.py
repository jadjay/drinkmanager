from __future__ import unicode_literals

from django.contrib import admin
from django.db import models

from django.core.files import File

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
from jsonfield import JSONField



try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


try:
    from io import BytesIO as cStringIO
except ImportError:
    import cStringIO

class Drink(models.Model):
    
    name = models.CharField(max_length=40)
    ean13 = models.CharField(max_length=40,default="")
    photo = models.ImageField(upload_to='uploads/',default="uploads/canette.jpg")
    description = JSONField(null=True,blank=True,)

    def __str__(self):
        return "%s" % self.name

    def lastStock(self):
        if not self.stock_set.all():
            return None
        return self.stock_set.latest('date')

    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        # do_something_else()

class Stock(models.Model):

    date = models.DateField()
    quantity = models.IntegerField()
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.date.strftime("%F"),self.drink.name,self.quantity)


class Consumption(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    
    def __str__(self):
        return "%s %s %s" % (self.date.strftime("%FT%T"),self.user.username,self.drink.name)

    def getuser(self):
        return self.user

##  class ConsumptionAdmin(admin.ModelAdmin):
##      list_display = ('date','drink','user')
##  #    list_filter = ('user__username', 'drink__name')
##  #    search_fields = ('user__username','drink__name')
