# src/app/shop/admin.py

# Django dan third parties modules
from django.contrib import admin
from django.utils.html import format_html

# Locals
from app.shop.models import Slider, Collection, Category, Image

# Register your models here.

# admin.site.register(Slider)

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')

    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')

    display_image.short_description = 'image'

  
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')
    
    display_image.short_description = 'image'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_image')
    list_display_links = ('name',)
    
    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')
    
    display_image.short_description = 'image'
    exclude = ('slug',)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

admin.site.register(Slider, SliderAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
