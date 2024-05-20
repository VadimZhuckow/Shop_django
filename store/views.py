from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseNotFound

from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import DATABASE

from logic.services import filtering_category


def shop_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        with open('store/shop.html', encoding='utf-8') as f:
            data = f.read()
        return HttpResponse(data)


def products_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        id_cart = request.GET.get('id')
        category_key = request.GET.get('category')
        ordering_key = request.GET.get('ordering')
        if id_cart in DATABASE.keys():
            return JsonResponse(DATABASE.get(id_cart),
                                json_dumps_params={
                                    "indent": 4,
                                    "ensure_ascii": False
                                })
        if ordering_key:
            if request.GET.get('reverse') and request.GET.get('reverse').lower() == 'true':
                data = filtering_category(DATABASE, category_key, ordering_key, True)
            else:
                data = filtering_category(DATABASE, category_key, ordering_key)
        else:
            data = filtering_category(DATABASE, category_key)
        return JsonResponse(
            data,
            safe=False,
            json_dumps_params={
                "indent": 4,
                "ensure_ascii": False
            }
        )


def products_page_view(request: HttpRequest, page: [str, int]) -> HttpResponse:
    if request.method == "GET":
        if isinstance(page, int):
            data = DATABASE.get(str(page))
            if data:
                with open(f"store/products/{data['html']}.html", encoding="utf-8") as f:
                    page = f.read()
                return HttpResponse(page)
        if isinstance(page, str):
            for data in DATABASE.values():
                if data["html"] == page:
                    with open(f"store/products/{page}.html", encoding="utf-8") as f:
                        page = f.read()
                    return HttpResponse(page)
        if page not in DATABASE.values():
            return HttpResponseNotFound('Такого товара нет в базе')
