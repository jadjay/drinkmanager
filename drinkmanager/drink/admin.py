from django.contrib import admin
from django.core.mail import send_mail

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

admin.site.register(Drink)
admin.site.register(Stock)
admin.site.register(Consumption)

