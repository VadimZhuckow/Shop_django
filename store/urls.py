from django.urls import path
from .views import products_view, shop_view

urlpatterns = [
    path('product/', products_view),
    path('', shop_view),
]
