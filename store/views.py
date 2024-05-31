from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseNotFound

from django.http import HttpRequest, HttpResponse, JsonResponse

from django.shortcuts import redirect

from .models import DATABASE

from logic.services import filtering_category, view_in_cart, add_to_cart, remove_from_cart


def shop_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        # Обработка фильтрации из параметров запроса
        category_key = request.GET.get("category")
        if ordering_key := request.GET.get("ordering"):
            if request.GET.get("reverse") in ('true', 'True'):
                data = filtering_category(DATABASE, category_key, ordering_key,
                                          True)
            else:
                data = filtering_category(DATABASE, category_key, ordering_key)
        else:
            data = filtering_category(DATABASE, category_key)
        return render(request, 'store/shop.html',
                      context={"products": data,
                               "category": category_key})


def products_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        id_cart = request.GET.get('id')
        category_key = request.GET.get('category')
        ordering_key = request.GET.get('ordering')
        if id_cart:
            if id_cart in DATABASE.keys():
                return JsonResponse(DATABASE.get(id_cart),
                                    json_dumps_params={
                                        "indent": 4,
                                        "ensure_ascii": False
                                    })
            else:
                return HttpResponseNotFound('Такого товара нет в базе')
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


def cart_view(request):
    if request.method == "GET":
        data = view_in_cart()
        json_param = request.GET.get('format')
        if json_param and json_param.lower() == "json":
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})
        products = []
        for product_id, quantity in data['products'].items():
            product = DATABASE.get(product_id)
            product["quantity"] = quantity
            product["price_total"] = f"{quantity * product['price_after']:.2f}"
            products.append(product)
        return render(request, "store/cart.html", context={"products": products})


def cart_add_view(request, id_product):
    if request.method == "GET":
        result = add_to_cart(id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в корзину"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в корзину"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def cart_del_view(request, id_product):
    if request.method == "GET":
        result = remove_from_cart(id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def coupon_check_view(request, name_coupon):
    DATA_COUPON = {
        "coupon": {
            "value": 10,
            "is_valid": True},
        "coupon_old": {
            "value": 20,
            "is_valid": False},
        "coupon_new": {
            "value": 50,
            "is_valid": True}
    }
    if request.method == "GET":
        if name_coupon and name_coupon in DATA_COUPON:
            return JsonResponse({'discount': DATA_COUPON[name_coupon]['value'],
                                 'is_valid': DATA_COUPON[name_coupon]['is_valid']})
        return HttpResponseNotFound("Неверный купон")


def delivery_estimate_view(request):
    DATA_PRICE = {
        "Россия": {
            "Москва": {"price": 80},
            "Санкт-Петербург": {"price": 80},
            "Новгород": {"price": 20},
            "fix_price": 100,
        },
    }
    if request.method == "GET":
        data = request.GET
        country = data.get('country')
        city = data.get('city')
        if country in DATA_PRICE and city in DATA_PRICE[country]:
            return JsonResponse({'price': DATA_PRICE[country][city]['price']})
        if country in DATA_PRICE and city not in DATA_PRICE:
            return JsonResponse({'price': DATA_PRICE[country]['fix_price']})
        if country not in DATA_PRICE:
            return HttpResponseNotFound("Неверные данные")


def cart_buy_now_view(request, id_product):
    if request.method == "GET":
        result = add_to_cart(id_product)
        if result:
            return redirect("store:cart_view")

        return HttpResponseNotFound("Неудачное добавление в корзину")


def cart_remove_view(request, id_product):
    if request.method == "GET":
        result = remove_from_cart(id_product)
        if result:
            return redirect("store:cart_view")

        return HttpResponseNotFound("Неудачное добавление в корзину")
