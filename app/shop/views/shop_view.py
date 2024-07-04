# src/app/shop/views/shop_view.py

# Django dan third party modules
from django.shortcuts import render
from django.http import HttpResponse

# Locals
from app.shop.models.Slider import Slider
from app.shop.models.Collection import Collection
from app.shop.models.Product import Product


# Create your views here.

def index(request):

	sliders = Slider.objects.all()
	collections = Collection.objects.all()

	best_sellers = Product.objects.filter(is_best_seller=True)
	new_arrivals = Product.objects.filter(is_new_arrival=True)
	featured = Product.objects.filter(is_featured=True)
	special_offers = Product.objects.filter(is_special_offer=True)

	data = {
		"sliders":sliders,
		"collections":collections,
		"best_sellers":best_sellers,
		"new_arrivals":new_arrivals,
		"featured":featured,
		"special_offers":special_offers,
	}

	return render(request, "shop/index.html", data)