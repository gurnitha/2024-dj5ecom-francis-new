# src/app/shop/urls.py

# Django dan third parties modules
from django.urls import path

# Locals
from app.shop.views import shop_view

# app name
app_name = "shop"

urlpatterns = [
    path('', shop_view.index, name='home'),
    path('page/<str:slug>', shop_view.display_page, name='page'),
    path('prouct/<str:slug>', shop_view.display_product, name='single_product'),
    path('shop', shop_view.shop, name='shop_list'),
]