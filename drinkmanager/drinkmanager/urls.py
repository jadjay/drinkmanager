"""drinkmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.contrib import auth
from django.urls import path, include, re_path
from . import views
from drink import views as dviews

urlpatterns = [
    re_path(r'^$', dviews.index, name='index'),
    re_path(r'^drink/', include('drink.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/', include('django_registration.backends.activation.urls')),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/login/', auth.views.auth_login, name='login'),
    re_path(r'^accounts/logout/', auth.views.auth_logout, name='logout'),
#    re_path(r'logout/$', auth.views.auth_logout, name='logout'),
]
