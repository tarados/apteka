import json
import datetime
import re
import xlsxwriter
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
    workbook = xlsxwriter.Workbook(response)
    bold = workbook.add_format({'bold': True})
    no_bold = workbook.add_format({'bold': False})
    no_border = workbook.add_format({'bold': True})
    bold.set_border(1)
    no_bold.set_border(1)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'Наименование', bold)
    worksheet.set_column('A:A', 50)
    worksheet.write(0, 1, 'Количество', bold)
    worksheet.set_column('B:B', 12)
    worksheet.write(0, 2, 'Цена', bold)
    worksheet.set_column('C:C', 8)
    worksheet.write(0, 3, 'Сумма', bold)
    worksheet.set_column('D:D', 10)
    i = 1
    for order_content in OrderItem.objects.filter(order=order_id):
        worksheet.write(i, 0, str(order_content.product), no_bold)
        worksheet.write(i, 1, float(order_content.quantity), no_bold)
        worksheet.write(i, 2, float(order_content.price), no_bold)
        worksheet.write(i, 3, float(order_content.cost_product), no_bold)
        i += 1
    worksheet.write(i, 0, 'Всего:', no_border)
    worksheet.write(i, 3, '=SUM(D1:D4)', no_border)
    workbook.close()
    return response
