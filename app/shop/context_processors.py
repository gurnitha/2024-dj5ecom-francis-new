# app/shop/context_processors.py

# Locals
from app.shop.models.Setting import Setting
from app.shop.models.Social import Social
from app.shop.models.Page import Page

def site_settings(request):
    site_settings = Setting.objects.first()
    socials = Social.objects.all()
    head_pages = Page.objects.filter(is_head=True)
    foot_pages = Page.objects.filter(is_foot=True)

    my_socials = []
    for item in socials:
        my_socials.append({
            'name': item.name,
            'icon': item.icon,
            'link': item.link,
        })

    my_head_pages = []
    for item in head_pages:
        my_head_pages.append({
            'name': item.name,
            'slug': item.slug
        })

    my_foot_pages = []
    for item in foot_pages:
        my_foot_pages.append({
            'name': item.name,
            'slug': item.slug
        })

    data = {
        'name' : site_settings.name,
        'description' : site_settings.description,
        'email' : site_settings.email,
        'currency' : site_settings.currency,
        'phone' : site_settings.phone,
        'street' : site_settings.street,
        'city' : site_settings.city,
        'code_postal' : site_settings.code_postal,
        'state' : site_settings.state,
        'copyright' : site_settings.copyright,
        'socials': my_socials,
        'head_pages': my_head_pages,
        'foot_pages': my_foot_pages,
    }
    request.session.update(data)
    
    return data