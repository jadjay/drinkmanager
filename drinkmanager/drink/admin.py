from django.contrib import admin

# Register your models here.
from .models import Drink, Stock, Consumption

class ConsumptionAdmin(admin.ModelAdmin):

    list_display = ['date','drink','user']

    list_filter = ('user__username', 'drink__name')

    search_fields = ('user__username','drink__name')














admin.site.register(Drink)
admin.site.register(Stock)
admin.site.register(Consumption, ConsumptionAdmin)

