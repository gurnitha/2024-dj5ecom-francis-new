# src/app/shop/models/Slider.py

# Django dan third parties modules
from django.db import models


# Models: Collection
class Collection(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    description = models.CharField(max_length=120, blank=False, null=False)
    button_text = models.CharField(max_length=60, blank=False, null=False)
    button_link = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to="sliders/%Y/%m/%d/", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)