from django.contrib import admin

from datetime import datetime

# Register your models here.
from .models import Drink, Stock, Consumption


from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template.loader import render_to_string
@admin.action(description='Send mail to users')
def user_send_mail(modeladmin, request, queryset):


    conso_per_user={}
    for conso in queryset:
        if not conso.user.email in conso_per_user.keys():
            conso_per_user[conso.user.email]={ 
                    "user": conso.user,
                    "nb": 1
                    }
        else:
            conso_per_user[conso.user.email]['nb']+=1

    for email,user in conso_per_user.items():
        user['euro'] = user['nb']/2
        msg_plain = render_to_string('drink/mail_ta_conso.txt', {'email': email, 'user': user})
        msg_html = render_to_string('drink/mail_ta_conso.html', {'email': email, 'user': user})
#templates/drink/
        send_mail(
            "%s - Ta conso aujourd'hui" % user['user'].username,
            msg_plain,
            'noreply@rachetjay.fr',
            [ email ],
            html_message=msg_html,
            fail_silently=False,
        )

@admin.action(description='Get info from openfoodfacts')
def get_openfoodfacts(modeladmin, request, queryset):
    for drink in queryset.all():
        drink.getopenfoodfacts()

class DrinkAdmin(admin.ModelAdmin):
    fields = ['ean13','name','photo','description']
    list_display = ['name', 'ean13']
    search_fields = ['name']
    ordering = ['name']
    actions = [get_openfoodfacts]

class StockAdmin(admin.ModelAdmin):
    fields = ['date','drink','quantity']
    list_display = ['drink','quantity','date']
    search_fields = ['drink__name']
    list_filter = ['drink__name']

class ConsumptionAdmin(admin.ModelAdmin):
    fields = ['user','drink']
    #list_display = ['date','user','drink']
    list_display = ['date','user','drink','la_conso']
    search_fields = [ 'user__username']
    list_filter = ('drink__name','user__username')
    actions = [user_send_mail]

admin.site.register(Stock, StockAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(Consumption, ConsumptionAdmin)
