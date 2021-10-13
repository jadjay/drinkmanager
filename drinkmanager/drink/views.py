from datetime import datetime,timedelta
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Drink, Stock, Consumption
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext



# Create your views here.

def index(request):
     drinks = Drink.objects.all
     context = { 'drinks': drinks }
     return render(request, 'drink/index.html', context)

def prints(request):
     drinks = Drink.objects.all
     context = { 'drinks': drinks }
     return render(request, 'drink/print.html', context)

@login_required
def take(request, drink_name):

    if request.user.is_authenticated():
        now,onehour = datetime.now(),timedelta(hours=1)
        onehourago = now-onehour

        cookie = {
		"name": "drinkmanager_%s" % drink_name,
		"value": "%s" % (now).strftime("%c")
	}

	cookieval = request.COOKIES.get(cookie['name']) if request.COOKIES.get(cookie['name']) else (now-onehour-onehour).strftime("%c")
        lasttaketime = datetime.strptime('%s' % cookieval,"%c")

        if lasttaketime > onehourago :
            return tosoon(request,drink_name,lasttaketime)

	#session.set_cookie('%s' % cookie['name'], '%s' % cookie['value'])


        drink = Drink.objects.get(name=drink_name)
        context = { 'drink': drink }
	html = render(request, 'drink/sure.html', context)
	html.set_cookie('%s' % cookie['name'], '%s' % cookie['value'])
        return html
    else:
        return redirect('auth_login')

@login_required
def taken(request, drink_name):
        mydrink = Drink.objects.get(name=drink_name)
        mystock = mydrink.lastStock()
        if mystock:
            mystock.quantity -= 1
            mystock.save()
            myconso=Consumption.objects.create(drink=mydrink,user=request.user)
        return show(request,drink_name)

@login_required
def maconso(request):
    drinks = Drink.objects.all
    consos = Consumption.objects.filter(user=request.user)
    context = {
        'drinks': drinks,
        'consos': consos,
    }
    return render(request, 'drink/maconso.html', context)

@login_required
def conso(request):
    drinks = Drink.objects.all()
    consos = Consumption.objects.all()
    users = User.objects.all()
    byuser = []
    for user in users:
        byuser.append(
            { 
                'name': user.username,
                'conso': consos.filter(user=user).count(),
            }
        )
    bydrink = []
    for drink in drinks:
        bydrink.append(
            { 
                'name': drink.name,
                'conso': consos.filter(drink=drink).count(),
            }
        )
    context = {
        'bydrink': bydrink,
        'byuser': byuser,
    }
    return render(request, 'drink/conso.html', context)

@login_required
def stock(request, drink_name):
    drink = Drink.objects.filter(name=drink_name)
    consos = Consumption.objects.filter(drink=drink)
    context = {
        'drinks': drink,
        'consos': consos,
    }
    return render(request, 'drink/stock.html', context)

def show(request, drink_name):
    mydrink = Drink.objects.get(name=drink_name)
    context = {
        'drink': mydrink,
    }
    return render(request, 'drink/show.html', context)

def tosoon(request, drink_name, lasttaketime):
    mydrink = Drink.objects.get(name=drink_name)
    context = {
        'drink': mydrink,
        'lasttaketime': lasttaketime,
    }
    return render(request, 'drink/tosoon.html', context)



def handler404(request, *args, **argv):
    response = render_to_response('drink/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('drink/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

