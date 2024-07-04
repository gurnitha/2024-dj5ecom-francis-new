# src/app/shop/urls.py

# Django dan third parties modules
from django.urls import path

# Locals
from app.shop.views.shop_view import index

# app name
app_name = "shop"

urlpatterns = [
    path('', index, name='home'),
]