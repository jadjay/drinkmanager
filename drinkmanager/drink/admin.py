from django.contrib import admin
from django.core.mail import send_mail

from datetime import datetime

#	def user_send_mail
#	send_mail(
#	    'Subject here',
#	    'Here is the message.',
#	    'from@example.com',
#	    ['to@example.com'],
#	    fail_silently=False,
#	)

# Register your models here.
from .models import Drink, Stock, Consumption


class StockAdmin(admin.ModelAdmin):
    fields = ['date','drink','quantity']
    list_display = ['drink','quantity','date']
    search_fields = ['drink__name']
    list_filter = ['drink__name']

class DrinkAdmin(admin.ModelAdmin):
    fields = ['name','photo','description']
    list_display = ['name','description']
    search_fields = ['name']
    list_filter = ['name']

class ConsumptionAdmin(admin.ModelAdmin):
    fields = ['date','user','drink']
    #list_display = ['date','user','drink']
    list_display = ['date','user','drink','la_conso']
    search_fields = [ 'user__username']
    list_filter = ('drink__name','user__username')

admin.site.register(Stock, StockAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(Consumption, ConsumptionAdmin)

