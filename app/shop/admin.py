# src/app/shop/admin.py

# Django dan third parties modules
from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from ckeditor.widgets import CKEditorWidget

# Locals
from app.shop.models import (
    Slider, Collection, Category, 
    Image, Product, Setting, 
    Social, Page, NavCollection)


# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)

    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="150" />')

    display_image.short_description = 'image'

  
class NavCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title',)
    
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
        return format_html(f'<img src="{ obj.image.url }" height="50" width="60" />')
    
    display_image.short_description = 'image'
    exclude = ('slug',)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('id', 'name', 'sold_price', 'is_best_seller','is_featured', 'is_special_offer', 'is_new_arrival', 'regular_price', 'display_image')
    list_display_links = ('name',)
    list_editable = ('is_best_seller','is_featured', 'is_special_offer', 'is_new_arrival')
    list_per_page = 5
    
    def display_image(self, obj):
        first_image = obj.images.first()
        if not first_image:
            return ''
        return format_html(f'<img src="{ first_image.image.url }" height="90" width="80" />')
    
    exclude = ('slug',)
    display_image.short_description = 'image'
    
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'display_logo', 'street', 'city')
    list_display_links = ('name',)
    
    def display_logo(self, obj):
        return format_html(f'<img src="{ obj.logo.url }" width="20" />')
    
    display_logo.short_description = 'logo'


class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'link')
    list_display_links = ('name',)
    

class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_head', 'is_foot', 'is_checkout')
    list_display_links = ('name',)
    list_editable = ('is_head', 'is_foot', 'is_checkout')
    
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    exclude = ('slug',)

    
admin.site.register(Slider, SliderAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(NavCollection, NavCollectionAdmin)
