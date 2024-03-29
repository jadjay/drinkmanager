from __future__ import unicode_literals


from django.contrib import admin
from django.db import models

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from django.contrib.sites.shortcuts import get_current_site

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
from jsonfield import JSONField

import os
import requests
import re
import urllib
import unidecode

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


try:
    from io import BytesIO as cStringIO
except ImportError:
    import cStringIO

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_openff(description):
    pass

    #problemes = [
    #            'nom',
    #            'quantite',
    #            'ingredient',
    #            'nutriscore_grade',
    #            ]

    #for probleme in problemes:
    #    if probleme not in description.keys():
    #        raise ValidationError( _("%(probleme)s n'est pas défini" ), params={'probleme': probleme},)


class Drink(models.Model):
    
    ean13 = models.CharField(max_length=40,blank=True)
    name = models.CharField(max_length=40,blank=True)
    photo = models.ImageField(upload_to='uploads/',default="uploads/canette.jpg")
    description = JSONField(null=True,blank=True,validators=[validate_openff])
    crible = [
        'product_name_fr',
        'quantity',
        'ingredients',
        'nutriscore_grade',
        'nutriscore_data',
        'selected_images',
        ]

    def __str__(self):
        return "%s" % self.name

    def lastStock(self):
        if not self.stock_set.all():
            return None
        return self.stock_set.latest('date')

    def getopenfoodfacts(self):
        if self.ean13:

            # API OpenFoodFacts -> code produit
            offurl='http://fr.openfoodfacts.org/api/v0/product/%s.json' % self.ean13
            #print(url)

            # On récupère la partie product du json d'off
            response = requests.get(offurl)
            off_infos = response.json()['product']

            # On ajoute que ce qui nous intéresse dans resultat
            resultat = {}
            for myinfo in self.crible:
                if myinfo in off_infos.keys():
                    resultat[myinfo] = off_infos[myinfo]
                else:
                    resultat[myinfo] = 'unknown'

            #for infok,infov in off_infos.items():
            #    if infok in self.crible:
            #        resultat[infok] = infov
            #    else:
            #        resultat[infok] = 'unknown'

            # On trie les ingrédients
            resultat['ingredients'] = sorted(resultat['ingredients'], key = lambda x: float(x['percent_estimate']),reverse=True)


            # On défini l'image nutriscore
            # Doc
            # https://static.openfoodfacts.org/images/misc/nutriscore-a.svg
            resultat['nutriscore_image_url'] = 'images/nutriscore-%s.svg' % resultat['nutriscore_grade'] 

            
            # On tente de récupérer l'image du produit
            try:
                if 'fr' in resultat['selected_images']['front']['display'].keys():
                    product_image_url = resultat['selected_images']['front']['display']['fr']
                elif 'en' in resultat['selected_images']['front']['display'].keys():
                    product_image_url = resultat['selected_images']['front']['display']['en']
                else:
                    product_image_url = 'https://media.istockphoto.com/photos/senior-man-shrugging-shoulders-picture-id91520053?k=20&m=91520053&s=612x612&w=0&h=W8iwQM7C7hFrF9Z2aY3g0Or1ewB9Mb_uALyiI0DBbtQ='

                product_image = urllib.request.urlopen(product_image_url)

            except Exception as e:
                print(e)
                product_image_url = 'https://media.istockphoto.com/photos/senior-man-shrugging-shoulders-picture-id91520053?k=20&m=91520053&s=612x612&w=0&h=W8iwQM7C7hFrF9Z2aY3g0Or1ewB9Mb_uALyiI0DBbtQ='

                product_image = urllib.request.urlopen(product_image_url)

            if 'product_name_fr' in resultat.keys():
                self.name = re.sub(r'\s+','_', resultat['product_name_fr'])
            elif 'product_name_en' in resultat.keys():
                self.name = re.sub(r'\s+','_', resultat['product_name_en'])
            else:
                self.name = re.sub(r'\s+','_', resultat['product_name'])

            #self.photo.save(u'%s.jpg' % self.name, File(product_image.read()),save=False)
            self.photo.save(u'%s.jpg' % self.name, product_image, save=False)

            self.description = resultat

            #try:
            #    self.clean_fields()
            #except ValidationError as e:
            #    self.description['nutriscore_grade'] = 'unknown'
            #    pass

            self.save()
        else:
            resultat = { }
            self.save()


            #if ('product_name_fr','quantity','ingredients','nutriscore_grade','nutriscore_data') in product['product'].keys():
            #    drink_name = re.sub(r'\s+','_',product['product']['product_name_fr'])
            #    resultat = { 
            #        "nom":          product['product']['product_name_fr'],
            #        "quantite":     product['product']['quantity'],
            #        "ingredient":   product['product']['ingredients'],
            #        "nutriscore": { 
            #                "grade":        product['product']['nutriscore_grade'],
            #                "data":         product['product']['nutriscore_data'],
            #                "image_url":    'images/nutriscore-%s.svg' % product['product']['nutriscore_grade']
            #        }
            #    }
            #    self.name = drink_name
            #    self.description = resultat
            #    if ('fr') in product['product']['selected_images']['front']['display'].keys():
            #        drink_image_url = product['product']['selected_images']['front']['display']['fr']
            #        
            #        img_temp = NamedTemporaryFile(delete=True)
            #        img_temp.write(urllib.request.urlopen(drink_image_url).read())
            #        img_temp.flush()
            #        
            #        self.photo.save('%s.jpg' % drink_name, File(img_temp))
            #    else:
            #        self.save()
            #else:
            #    self.name = "Fiche incomplete sur OpenFF"
            #    self.description = { "status": "Unknown",
            #                         "elements_manquants": [],
            #                         "comment": "Merci de compléter la fiche",
            #                         "url": "https://fr.openfoodfacts.org/produit/%s" % self.ean13 }

            #    for elem in ('product_name_fr','quantity','ingredients','nutriscore_grade','nutriscore_data'):
            #        if not elem in product['product'].keys():
            #            self.description['elements_manquants'].append(elem)

            #    self.save()



        #else:
        #    resultat = { }



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

    # Display admin 
    def la_conso(obj):
        return ("%s---%s---%s" % (obj.date.strftime('%Y-%m-%d_%H:%M'),obj.user, obj.drink)).lower()

    la_conso.admin_order_field = 'date'
    la_conso.short_description = 'Ticket Consommation'
