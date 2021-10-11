from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="drink-index"),
    url(r'^maconso/$', views.maconso, name="drink-maconso"),
    url(r'^conso/$', views.conso, name="drink-conso"),
    url(r'^print/$', views.prints, name="drink-print"),
    url(r'^take/(?P<drink_name>\w{2,})', views.take, name="drink-take"),
    url(r'^taken/(?P<drink_name>\w{2,})', views.taken, name="drink-taken"),
    url(r'^show/(?P<drink_name>\w{2,})', views.show, name="drink-show"),
    url(r'^stock/(?P<drink_name>\w{2,})', views.stock, name="drink-stock"),
]

handler404 = 'drink.views.handler404'
handler500 = 'drink.views.handler500'
