from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Drink, Stock, Consumption
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


# Create your views here.

def index(request):
#    if request.user.is_authenticated():
     drinks = Drink.objects.all
     context = { 'drinks': drinks }
     return render(request, 'drink/index.html', context)
#    else:
#        return redirect('auth_login')

@login_required
def take(request, drink_name):
    if request.user.is_authenticated():
        mydrink = Drink.objects.get(name=drink_name)
        mystock=mydrink.lastStock()
        mystock.quantity -= 1
        mystock.save()
        myconso=Consumption.objects.create(drink=mydrink,user=request.user)
        return show(request,drink_name)
    else:
        return redirect('auth_login')

def show(request, drink_name):
    mydrink = Drink.objects.get(name=drink_name)
    context = {
        'drink': mydrink
    }
    return render(request, 'drink/show.html', context)

