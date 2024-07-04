# src/app/shop/models/Image.py

# Django dan third parties modules
from django.db import models

# Locals
from app.shop.models.Product import Product


# Model:Image
class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/%Y/%m/%d/", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)