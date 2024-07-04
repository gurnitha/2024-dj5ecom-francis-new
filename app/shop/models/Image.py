# src/app/shop/models/Image.py

# Django dan third parties modules
from django.db import models


# Model:Image
class Image(models.Model):
    image = models.ImageField(upload_to="products/%Y/%m/%d/", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)