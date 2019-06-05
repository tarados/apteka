import os
from conf.settings import BASE_DIR
import xml.dom.minidom
import json
from bs4 import BeautifulSoup
import re


def priceXml():
    file = os.path.join(BASE_DIR, 'static', 'price.xml')
    dom = xml.dom.minidom.parse(file)
    dom.normalize()
    proposals = dom.getElementsByTagName("Предложение")
    pricelist = []
    for i in range(len(proposals)):
        name = proposals[i].getElementsByTagName("Наименование")[0]
        price = proposals[i].getElementsByTagName("ЦенаЗаЕдиницу")[0]
        n = name.firstChild.data
        p = price.firstChild.data.replace('\xa0', '')
        price_dic = {
            "model": "app.Price",
            "pk": i,
            "fields": {
                "price_name": n,
                "price_rate": float(p.replace(',', '.')),
                "price_photo": ""
            }
        }
        pricelist.append(price_dic)
    file_out = os.path.join(BASE_DIR, 'app', 'fixture', 'fixture.json')
    with open(file_out, 'w') as outfile:
        json.dump(pricelist, outfile)
    return pricelist


def priceHtml():
    contents = os.path.join(BASE_DIR, 'static', 'price.html')
    priceList = []
    with open(contents, 'rb') as outfile:
        data = outfile.read().decode('utf8')
    soup = BeautifulSoup(data, "html.parser")
    i = 1
    for contents in soup('tr', {'class': 'R5'}):
        n = contents.find('td', {'class': 'R5C0'}).text
        manufacturer = contents.find('td', {'class': 'R5C1'}).text
        p = contents.find('td', {'class': 'R5C2'}).text.replace('\xa0', '')
        price_dic = {
            "model": "app.Price",
            "pk": i,
            "fields": {
                "price_name": n,
                "price_rate": float(p.replace(',', '.')),
                "price_photo": "",
                "price_manufacturer": manufacturer
            }
        }
        i += 1
        priceList.append(price_dic)
    file_out = os.path.join(BASE_DIR, 'app', 'fixture', 'fixture.json')
    with open(file_out, 'w') as outfile:
        json.dump(priceList, outfile)
    return priceList


priceHtml()

# priceXml()


"""Обновление прайса производим по схеме:
 1. Загружаем новый прайс с именем price.xml в папку static
 2. На всякий случай удаляем файл app/fixture/fixture.json
 3. Выполняем priceXml() или priceHtml().
 4. В папке app/fixture/ должен появиться новый файл fixture.json
 5. В терминале выполяем  python manage.py loaddata fixture.json
  """