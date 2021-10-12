from django.contrib import admin

# Register your models here.
from .models import Drink, Stock, Consumption

class ConsumptionAdmin(admin.ModelAdmin):

    list_display = ['date','drink','user']

    list_filter = ('user__username', 'drink__name')

    search_fields = ('user__username','drink__name')


@admin.action(description='Get info from openfoodfacts')
def get_openfoodfacts(modeladmin, request, queryset):
    for drink in queryset.all():
        drink.getopenfoodfacts()

class DrinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'ean13']
    ordering = ['name']
    actions = [get_openfoodfacts]











admin.site.register(Drink, DrinkAdmin)
admin.site.register(Stock)
admin.site.register(Consumption, ConsumptionAdmin)

