import json
import datetime
from django.http import JsonResponse
from app.models import Product, Farmacy, Order, OrderItem


def index(request):
    # TODO: убрать дублирование кода
    # TODO: поставить ограничение при фильтрации 100-200 строк
    # TODO: если нет фильтра то выдавать какой-то набор популярных товаров

    products_result = []
    if request.GET:
        query = request.GET.get('query').upper()
        if query != '':
            products = Product.objects.filter(product_name__icontains=query)[:10]
        else:
            products = Product.objects.all()[:5]
        for product in products:
            products_result.append(
                {'title': product.product_name,
                 'manufacturer': product.product_manufacturer,
                 'price': product.price,
                 'productId': product.id
                 # 'product_photo': product.product_photo.url
                 })
    return JsonResponse({'products': products_result})


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
                'longitude': pharmacy.longitude,
                'pharmacyId': pharmacy.id
            })
    return JsonResponse({'pharmacyes': payload})


def orders(request):
    order_str = request.body.decode()
    order_content = json.loads(order_str)
    order = Order(
        date=datetime.datetime.now(),
        pharmacy=Farmacy.objects.get(id=order_content["pharmacyId"]),
        customer_name=order_content["name"],
        customer_surname=order_content["surname"],
        customer_phone=order_content["phone"]
    )
    order.save()
    order_total_sum = 0
    for order_item in order_content["order"]:
        product = Product.objects.get(id=int(order_item["productId"]))
        current_price = product.price
        if current_price >= order_item["price"]:
            product_price = current_price
        else:
            product_price = order_item["price"]
        order_item = OrderItem(
            order=Order.objects.get(id=order.id),
            product=product,
            quantity=order_item["quantity"],
            price=product_price,
            cost_product=product_price * order_item["quantity"],
        )
        order_item.save()
        order_total_sum = order_total_sum + order_item.cost_product
    order.total_price = order_total_sum
    order.save()
    return JsonResponse({'successful': 'successful'})
