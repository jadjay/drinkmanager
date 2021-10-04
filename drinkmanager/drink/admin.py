from django.contrib import admin

# Register your models here.
from .models import Drink, Stock, Consumption

admin.site.register(Drink)
admin.site.register(Stock)
admin.site.register(Consumption)

class ConsumptionAdmin(admin.ModelAdmin):
    model = Consumption
    list_display = ('date','drink','user')
    list_filter = ('user__username', 'drink__name')
    search_fields = ('user__username','drink__name')
