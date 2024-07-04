# src/app/shop/views/shop_view.py

# Django dan third party modules
from django.shortcuts import render
from django.http import HttpResponse

# Locals
from app.shop.models import Slider 

# Create your views here.

def index(request):

	sliders = Slider.objects.all()

	data = {
		"sliders":sliders
	}

	return render(request, "shop/index.html", data)