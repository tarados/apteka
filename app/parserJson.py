import requests
import xlwt
import re
import os
from conf.settings import BASE_DIR
from bs4 import BeautifulSoup

URL = 'https://www.olx.ua/nedvizhimost/kommercheskaya-nedvizhimost/arenda-kommercheskoy-nedvizhimosti/donetsk/?search%5Bfilter_float_total_area%3Afrom%5D=50&search%5Bfilter_float_total_area%3Ato%5D=200'


def get_http(url):
    response = requests.get(url)
    return response.text


def get_page_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('div', class_="pager rel clr")
    return int(pagination.find_all('a')[-2].text.strip())


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='fixed offers breakword redesigned')

    ads = []

    for rows in table.find_all('tr', class_="wrap"):
        link = rows.find('a')['href']
        if link:
            soupChild = BeautifulSoup(get_http(link), 'html.parser')
            titlebox = soupChild.find('div', class_="offer-titlebox")
            pricebox = soupChild.find('div', class_="pricelabel tcenter")
            titleboxDetails = soupChild.find('div', class_="offer-titlebox__details")
            # numberAd = titleboxDetails.em.small.text
            title = titlebox.h1.text.strip()
            price = pricebox.text.strip()

            adLists = []

            for tableChild in soupChild.find_all('table', class_="item"):
                childRow = tableChild.find('tr')
                caption = childRow.th.text.strip()
                try:
                    regex = re.compile(r'[\n\r\t]')
                    valueForCaption = re.sub(r'\s+', ' ', regex.sub(" ", tableChild.td.strong.text))
                except AttributeError:
                    valueForCaption = 'Пусто'
                adLists.append({
                    caption: valueForCaption.strip()
                })
            ads.append({
                'title': title,
                'price': price,
                'descriptions': [adList for adList in adLists]
            })
    for ad in ads:
        for a in ad['descriptions']:
            for x, y in a.items():
                ad[x] = y
        ad.pop('descriptions')
    return ads


def save(projects, path):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test')
    ws.write(0, 0, '№ п/п')
    ws.write(0, 1, 'title')
    ws.write(0, 2, 'price')
    ws.write(0, 3, 'Общая площадь')
    ws.write(0, 4, 'Этаж')
    ws.write(0, 5, 'Этажность')
    ws.write(0, 6, 'Тип недвижимости')
    ws.write(0, 7, 'Расположение')
    ws.write(0, 8, 'Ремонт')
    for i in range(len(projects)):
        ws.write(i + 1, 0, i + 1)
        ws.write(i + 1, 1, projects[i]['title'])
        ws.write(i + 1, 2, projects[i]['price'])
        try:
            ws.write(i + 1, 3, projects[i]['Общая площадь'])
        except KeyError:
            pass
        try:
            ws.write(i + 1, 4, projects[i]['Этаж'])
        except KeyError:
            pass
        try:
            ws.write(i + 1, 5, projects[i]['Этажность'])
        except KeyError:
            pass
        try:
            ws.write(i + 1, 6, projects[i]['Тип недвижимости'])
        except KeyError:
            pass
        try:
            ws.write(i + 1, 7, projects[i]['Расположение'])
        except KeyError:
            pass
        try:
            ws.write(i + 1, 8, projects[i]['Ремонт'])
        except KeyError:
          pass
        # i += 1
    fileout = os.path.join(BASE_DIR, 'aaa.xls')
    wb.save(fileout)


page_count = get_page_count(get_http(URL))
print('Всего найдено страниц %d' % page_count)
ads = []
for page in range(1, page_count + 1):
    print('Парсинг %d%%' % (page / page_count * 100))
    ads.extend(parse(get_http(URL + '&page=%d' % page)))

save(ads, 'aaa.xls')
