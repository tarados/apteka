import json
import datetime
import re
import xlwt
from django.http import  HttpResponse
from django.http import JsonResponse
from app.models import Product, Pharmacy, Order, OrderItem


def products(request):
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


def pharmacy(request):
    payload = []
    pharmacyes = Pharmacy.objects.all()
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


def order(request):
    order_str = request.body.decode()
    order_content = json.loads(order_str)
    print(order_content)
    order = Order(
        date=datetime.datetime.now(),
        pharmacy=Pharmacy.objects.get(id=order_content["pharmacyId"]),
        customer_name=order_content["name"],
        customer_surname=order_content["surname"],
        customer_phone=order_content["phone"]
    )
    order.save()
    print(order.status)
    order_total_sum = 0
    for order_item in order_content["order"]:
        product = Product.objects.get(id=int(order_item["productId"]))
        current_price = product.price
        if current_price >= order_item["price"]:
            product_price = current_price
        else:
            product_price = order_item["price"]
        order_item = OrderItem(
            order=order,
            product=product,
            quantity=order_item["quantity"],
            price=product_price,
            cost_product=product_price * order_item["quantity"],
        )
        order_item.save()
        order_total_sum = order_total_sum + order_item.cost_product
    order.total_price = order_total_sum
    order.save()
    return JsonResponse({'success': True})


def file_order_create(request, order_id):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    order = Order.objects.get(id=order_id)
    pharmacy_name = re.search(r'\d{1,2}', order.pharmacy.pharmacy_name)
    response['Content-Disposition'] = 'attachment; filename=%s%s%s.xlsx' % (order.date.strftime("%d%m%y"), '_A_', str(pharmacy_name.group()))
    book = xlwt.Workbook(encoding="utf-8")
    font_size_style = xlwt.easyxf('font: name Calibri, bold on, height 280;', 'cell: width 80;')

    sheet1 = book.add_sheet("Sheet 1")
    # sheet1.set_column(0, 0, 50)   # Column  A   width set to 20.
    # sheet1.set_column(1, 1, 30)   # Columns B-D width set to 30.
    # sheet1.set_column(2, 2, 30)   # Columns B-D width set to 30.
    # sheet1.set_column(3, 3, 30)   # Columns B-D width set to 30.

    sheet1.write(0, 0, 'Наименование', font_size_style)
    sheet1.write(0, 1, 'Количество')
    sheet1.write(0, 2, 'Цена')
    sheet1.write(0, 3, 'Сумма')

    i = 1
    for order_content in OrderItem.objects.filter(order=order_id):
        sheet1.write(i, 0, str(order_content.product))
        i += 1
        print(order_content.product)

    book.save(response)

    # writer = csv.writer(response)
    # writer.writerow([order.date])
    # writer.writerow([order.pharmacy.pharmacy_name])
    # writer.writerow(['Наименование', 'Количество', 'Цена', 'Сумма'])
    # writer.writerow(['Наименование', 'Количество', 'Цена', 'Сумма'])

    return response
