from django.contrib import admin

# Register your models here.
from .models import Drink, Stock, Consumption

admin.site.register(Drink)
admin.site.register(Stock)
admin.site.register(Consumption)

