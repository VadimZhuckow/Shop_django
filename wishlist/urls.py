from django.urls import path
from .views import wishlist_view, wishlist_add_json, wishlist_del_json, wishlist_json, wishlist_remove_view
from store.views import products_page_view


app_name = 'wishlist'

urlpatterns = [
    path("wishlist/", wishlist_view, name="wishlist_view"),
    path("wishlist/api/", wishlist_json, name="wishlist_json"),
    path("wishlist/api/add/<str:id_product>", wishlist_add_json),
    path("wishlist/api/del/<str:id_product>", wishlist_del_json),
    path('product/<slug:page>.html', products_page_view, name='products_page_view'),
    path('wishlist/remove/<str:id_product>', wishlist_remove_view, name="remove_now")

]
