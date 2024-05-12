from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

import time
from datetime import datetime


def date(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        data = datetime.today()
        return HttpResponse(data.strftime('%d %m - %H:%M'))

# Create your views here.
