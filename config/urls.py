# src/config/urls.py

# Django dan third parties modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    # admin
    path("admin/", admin.site.urls),

    # shop
    path("", include("app.shop.urls", namespace="shop")),
]
