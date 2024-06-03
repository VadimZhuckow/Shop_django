"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import random

from django.contrib import admin

from django.urls import path, include

from django.urls import path

from django.http import HttpResponse, HttpRequest

from weather.views import get_weather
from app_datetime.views import date
from store.views import *


def random_view(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponse(round(random.uniform(1, 100), 4))


urlpatterns = [

    path('', include('store.urls')),
    path('', include('weather.urls')),
    path('admin/', admin.site.urls),
    path('random/', random_view),
    path('datatime/', date),
    path('login/', include('app_login.urls')),
]
