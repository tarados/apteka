import os
from conf.settings import BASE_DIR
from app.models import Product
import re


def parseNumber(value, as_int=False):
    try:
        number = float(re.sub('[^.\-\d]', '', value))
        if as_int:
            return int(number + 0.5)
        else:
            return number / 100
    except ValueError:
        return float('nan')  # or None if you wish


def priceTxt():
    contents = os.path.join(BASE_DIR, 'static', 'price.txt')
    with open(contents, 'rb') as outfile:
        data = outfile.read().decode('utf8')
    rows = data.split("\n")
    rows.pop(0)
    for row in rows:
        number = row.split('\t')[2].replace('\r', '')
        p = Product(
            product_name=row.split("\t")[0],
            product_manufacturer=row.split("\t")[1],
            price=parseNumber(number, as_int=False)
        )
        p.save()


def deletePrice():
    Product.objects.all().delete()



"""Обновление прайса производим по схеме:
 1. Загружаем новый прайс с именем price.xml в папку static
 5. В терминале выполяем  python manage.py price
  """
