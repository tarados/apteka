import os
import xlrd
import xlwt
from conf.settings import BASE_DIR
from app.models import Pharmacy


def loadfarmacy():
    filename = os.path.join(BASE_DIR, 'static', 'farmacy.xlsx')

    rb = xlrd.open_workbook(filename)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test')

    def is_number(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    # выбираем активный лист

    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    for i in range(1, len(vals)):
        if type(vals[i][3]) == float:
            house = int(vals[i][3])
        else:
            house = vals[i][3]
        f = Pharmacy(
            pharmacy_name=vals[i][0],
            city=vals[i][1],
            house=house,
            street=vals[i][2],
            state_province=vals[i][4],
            manager=vals[i][5],
            phone=vals[i][6],
            latitude=vals[i][7],
            longitude=vals[i][8]
        )
        f.save()


def deleteFarmacy():
    Pharmacy.objects.all().delete()


"""Загрузку списка аптек в БД производим по схеме:
 1. Загружаем список аптек с именем farmacy.xlsx в папку static
 5. В терминале выполяем  python manage.py farmacy
  """