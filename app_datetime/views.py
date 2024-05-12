from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from datetime import datetime


def date(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        data = datetime.now()
        return HttpResponse(data)

# Create your views here.
