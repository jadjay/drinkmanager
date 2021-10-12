from __future__ import unicode_literals

from django.contrib import admin
from django.db import models

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
from jsonfield import JSONField

import requests
import re
import urllib



try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


try:
    from io import BytesIO as cStringIO
except ImportError:
    import cStringIO

class Drink(models.Model):
    
    ean13 = models.CharField(max_length=40,blank=True)
    name = models.CharField(max_length=40,blank=True)
    photo = models.ImageField(upload_to='uploads/',default="uploads/canette.jpg")
    description = JSONField(null=True,blank=True,)

    def __str__(self):
        return "%s" % self.name

    def lastStock(self):
        if not self.stock_set.all():
            return None
        return self.stock_set.latest('date')

    def getopenfoodfacts(self):
        if self.ean13:
            url='http://fr.openfoodfacts.org/api/v0/product/%s.json' % self.ean13
            #print(url)
            response = requests.get(url)
            product = response.json()
            drink_name = re.sub(r'\s+','_',product['product']['product_name_fr'])
            resultat = { 
                "nom":          product['product']['product_name_fr'],
                "quantite":     product['product']['quantity'],
                "ingredient":   product['product']['ingredients'],
                "nutriscore": { 
                        "grade":        product['product']['nutriscore_grade'],
                        "data":         product['product']['nutriscore_data'],
                        "image_url":    'https://static.openfoodfacts.org/images/misc/nutriscore-%s.svg' % product['product']['nutriscore_grade']
                }
            }
            drink_image_url = product['product']['selected_images']['front']['display']['fr']
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib.request.urlopen(drink_image_url).read())
            img_temp.flush()
            
            self.name = drink_name
            self.description = resultat
            self.photo.save('%s.jpg' % drink_name, File(img_temp))
            #self.photo = File(img_temp)
            #self.photo = File(urllib.request.urlopen(drink_image_url).read())
            #self.photo.save('%s.jpg' % self.name, File(urllib2.urlopen('%s' % myimage )))


        else:
            resultat = { }
        # Doc
        # https://static.openfoodfacts.org/images/misc/nutriscore-a.svg



    def save(self, *args, **kwargs):
        # do_something()
        #self.getopenfoodfacts()
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
