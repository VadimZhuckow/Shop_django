from django.urls import path
from .views import products_view, shop_view, products_page_view

urlpatterns = [
    path('', shop_view),
    path('product/', products_view),
    path('product/<slug:page>.html', products_page_view),
]
