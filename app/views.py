from django.http import JsonResponse
from app.models import Product


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

