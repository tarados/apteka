from django.http import JsonResponse
from app.models import Product, Farmacy


def index(request):
    # TODO: убрать дублирование кода
    # TODO: поставить ограничение при фильтрации 100-200 строк
    # TODO: если нет фильтра то выдавать какой-то набор популярных товаров

    payload = []
    if request.GET:
        query = request.GET.get('query').upper()
        products = Product.objects.filter(product_name__icontains=query)
        for product in products:
            payload.append(
                {'product': product.product_name,
                 'manufacturer': product.product_manufacturer
                 })
    else:
        products = Product.objects.all()[:5]
        for product in products:
            payload.append(
                {'product': product.product_name,
                 'manufacturer': product.product_manufacturer
                 })
    return JsonResponse({'payload': payload})


def farmacy(request):
    payload = []
    pharmacyes = Farmacy.objects.all()
    for pharmacy in pharmacyes:
        payload.append(
            {
                'pharmacy_name': pharmacy.pharmacy_name,
                'city': pharmacy.city,
                'house': pharmacy.house,
                'street': pharmacy.street,
                'state_province': pharmacy.state_province,
                'manager': pharmacy.manager,
                'phone': pharmacy.phone,
                'latitude': pharmacy.latitude,
                'longitude': pharmacy.longitude
            })
    return JsonResponse({'pharmacyes': payload})
