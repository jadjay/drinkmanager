from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name="drink-index"),
    re_path(r'^maconso/$', views.maconso, name="drink-maconso"),
    re_path(r'^conso/$', views.conso, name="drink-conso"),
    re_path(r'^print/$', views.prints, name="drink-print"),
    re_path(r'^take/(?P<drink_name>.{2,})', views.take, name="drink-take"),
    re_path(r'^taken/(?P<drink_name>.{2,})', views.taken, name="drink-taken"),
    re_path(r'^show/(?P<drink_name>.{2,})', views.show, name="drink-show"),
    re_path(r'^stock/(?P<drink_name>.{2,})', views.stock, name="drink-stock"),
]
