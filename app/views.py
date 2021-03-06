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
            products = Product.objects.all()[:6]
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
    order = Order(
        date=datetime.datetime.now(),
        pharmacy=Pharmacy.objects.get(id=order_content["pharmacyId"]),
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
    merge_format = workbook.add_format({'bold': True})
    bold.set_border(1)
    no_bold.set_border(1)
    merge_format.set_align('center')
    merge_format.set_align('vcenter')
    worksheet = workbook.add_worksheet()

    worksheet.merge_range('A1:D1', 'Заказ №%d' % order_id, merge_format)
    worksheet.merge_range('A2:D2', 'Дата: %s' % str(order.date)[:10], no_border)
    worksheet.merge_range('A3:D3', 'Заказчик: %s %s, тел: %s' % (order.customer_surname, order.customer_name, order.customer_phone, ), no_border)
    worksheet.write(4, 0, 'Наименование', bold)
    worksheet.write(4, 1, 'Количество', bold)
    worksheet.write(4, 2, 'Цена', bold)
    worksheet.write(4, 3, 'Сумма', bold)

    i = 5
    width_column = []
    for order_content in OrderItem.objects.filter(order=order_id):
        worksheet.write(i, 0, str(order_content.product), no_bold)
        worksheet.write(i, 1, float(order_content.quantity), no_bold)
        worksheet.write(i, 2, float(order_content.price), no_bold)
        worksheet.write(i, 3, float(order_content.cost_product), no_bold)
        width_column.append(len(str(order_content.product)))
        i += 1
    width = sorted(width_column)

    worksheet.set_column('A:A', width[len(width) - 1] + 4)
    worksheet.set_column('B:B', 12)
    worksheet.set_column('C:C', 8)
    worksheet.set_column('D:D', 10)
    worksheet.set_row(0, 30)

    worksheet.write(i, 0, 'Всего:', no_border)
    worksheet.write(i, 3, float(order.total_price), no_border)
    workbook.close()
    return response
