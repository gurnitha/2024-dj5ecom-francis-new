# src/app/shop/admin.py

# Django dan third parties modules
from django.contrib import admin
from django.utils.html import format_html

# Locals
from app.shop.models import Slider

# Register your models here.

# admin.site.register(Slider)

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')

    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')

    display_image.short_description = 'image'

admin.site.register(Slider, SliderAdmin)