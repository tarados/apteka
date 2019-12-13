from django.http import JsonResponse
from app.models import Product, Farmacy


def index(request):
    # TODO: убрать дублирование кода
    # TODO: поставить ограничение при фильтрации 100-200 строк
    # TODO: если нет фильтра то выдавать какой-то набор популярных товаров

    productload = []
    if request.GET:
        query = request.GET.get('query').upper()
        if query != 'EMPTY':
            products = Product.objects.filter(product_name__icontains=query)[:10]
        else:
            products = Product.objects.all()[:5]
        for product in products:
            productload.append(
                {'product': product.product_name,
                 'manufacturer': product.product_manufacturer,
                 'price': product.price,
                 # 'product_photo': product.product_photo.url
                 })
    return JsonResponse({'productload': productload})


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
