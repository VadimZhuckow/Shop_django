from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import DATABASE


def products_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return JsonResponse(DATABASE,
                            json_dumps_params={
                                "indent": 4,
                                "ensure_ascii": False
                            })


def shop_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        with open('store/shop.html', encoding='utf-8') as f:
            data = f.read()
        return HttpResponse(data)
