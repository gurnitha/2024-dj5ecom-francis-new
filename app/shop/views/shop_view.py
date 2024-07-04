# src/app/shop/views/shop_view.py

# Django dan third party modules
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	return render(request, "shop/index.html")