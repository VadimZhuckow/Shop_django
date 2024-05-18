from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseNotFound

from .models import DATABASE




def products_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        id_cart = request.GET.get('id')
        if id_cart in DATABASE.keys():
            return JsonResponse(DATABASE.get(id_cart),
                                json_dumps_params={
                                    "indent": 4,
                                    "ensure_ascii": False
                                })
        if not id_cart:
            return JsonResponse(DATABASE,
                                json_dumps_params={
                                    "indent": 4,
                                    "ensure_ascii": False})
        if id_cart not in DATABASE.keys():
            return HttpResponse('Такого товара нет')


def shop_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        with open('store/shop.html', encoding='utf-8') as f:
            data = f.read()
        return HttpResponse(data)
