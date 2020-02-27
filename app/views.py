import json
import datetime
from django.http import JsonResponse
from app.models import Product, Farmacy, Customer, Order, OrderItem


def index(request):
    # TODO: убрать дублирование кода
    # TODO: поставить ограничение при фильтрации 100-200 строк
    # TODO: если нет фильтра то выдавать какой-то набор популярных товаров

    products_result = []
    if request.GET:
        query = request.GET.get('query').upper()
        if query != 'EMPTY':
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
    print(order_content)
    customer = Customer(
        customer_name=order_content["name"],
        customer_surname=order_content["surname"],
        customer_phone=order_content["phone"]
    )
    customer.save()
    catalog = Order(
        registry_customer=Customer.objects.get(customer_name=order_content["name"]),
        registry_date=datetime.datetime.now()
    )
    for order in order_content["order"]:
        current_price = Product.objects.get(id=order["productId"]).price
        if current_price >= order["price"]:
            product_price = current_price
        else:
            product_price = order["price"]
        order_item = OrderItem(
            order_product=Product.objects.get(id=order["productId"]).product_name,
            order_quantity_product=order["quantity"],
            order_price=product_price,
            order_pharmacy=Farmacy.objects.get(id=order["pharmacyId"]).pharmacy_name
        )


    return JsonResponse({'successful': 'successful'})
