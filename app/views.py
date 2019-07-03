from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app.models import Product
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


def index(request):
    payload = []
    if request.GET:
        query = request.GET.get('query').upper()
        products = Product.objects.filter(product_name__icontains=query)
        for product in products:
            payload.append(
                {'product': product.product_name, 'manufacturer': product.product_manufacturer, 'price': product.price})
    else:
        products = Product.objects.all()[:5]
        for product in products:
            payload.append(
                {'product': product.product_name, 'manufacturer': product.product_manufacturer, 'price': product.price})
    return JsonResponse({'payload': payload})
# Create your views here.
