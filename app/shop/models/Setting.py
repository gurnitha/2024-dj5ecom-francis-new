# src/app/shop/models/Setting.py

# Django dan third parties modules
from django.db import models


# Model:Setting
class Setting(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    currency = models.CharField(max_length=4, blank=False, null=False)
    taxe_rate = models.FloatField(blank=False, null=False)
    logo = models.ImageField(upload_to="settings/", blank=False, null=False)
    street = models.CharField(max_length=60, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    code_postal = models.CharField(max_length=60, blank=False, null=False)
    state = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    copyright = models.CharField(max_length=255, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name