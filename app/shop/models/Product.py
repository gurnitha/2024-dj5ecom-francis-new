# src/app/shop/models/Product.py

# Django dan third parties modules
from django.db import models
from django.utils.text import slugify


# Model:Product
class Product(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=120, blank=False, null=False)
    more_description = models.TextField(blank=True, null=True)
    additional_infos = models.TextField(blank=True, null=True)
    stock = models.IntegerField(blank=False, null=False)
    solde_price = models.FloatField(blank=False, null=False)
    regular_price = models.FloatField(blank=False, null=False)
    brand = models.CharField(max_length=60, blank=True, null=True)
    is_available = models.BooleanField(blank=False, null=False)
    is_best_seller = models.BooleanField(blank=False, null=False)
    is_new_arrival = models.BooleanField(blank=False, null=False)
    is_featured = models.BooleanField(blank=False, null=False)
    is_special_offer = models.BooleanField(blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs) 