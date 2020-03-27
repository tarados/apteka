from django.db import models
from django.utils.translation import gettext as _


class Pharmacy(models.Model):
    """Модель торговой точки"""

    pharmacy_name = models.CharField("Аптека", max_length=255)
    city = models.CharField(max_length=50, null=True)
    house = models.TextField(null=True)
    street = models.CharField(null=True, max_length=50)
    state_province = models.CharField(max_length=50, null=True)
    manager = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "Аптека"
        verbose_name_plural = "Аптеки"

    def __str__(self):
        return self.pharmacy_name


class Product(models.Model):
    """Модель прайс"""

    product_name = models.CharField(max_length=250, db_index=True)
    product_manufacturer = models.CharField(max_length=250, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    product_photo = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name = "Наименование"
        verbose_name_plural = "Номенклатура"

    def __str__(self):
        return self.product_name


class Order(models.Model):
    """Модель Заказ"""

    date = models.DateTimeField("Дата заказа", null=True, blank=True)
    total_price = models.FloatField("Сумма заказа", null=True, blank=True)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Аптека")
    customer_name = models.CharField("Имя", max_length=12)
    customer_surname = models.CharField("Фамилия", max_length=20)
    customer_phone = models.CharField("Телефон", max_length=20)
    status = models.IntegerField("Статус", choices=((1, _("Новый")),
                                        (2, _("В обработке")),
                                        (3, _("Выполнен"))), default=1)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    """Модель Контент заказа"""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField("Цена", null=True, blank=True)
    quantity = models.FloatField("Количество", null=True, blank=True)
    cost_product = models.FloatField("Сумма", null=True, blank=True)


class ProductAvailability(models.Model):
    """Модель Наличие товара"""

    class Meta:
        db_table = 'product_availability'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="available")
    farmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    number = models.FloatField(null=True, blank=True)


def test():
    data = [
        {"name": "АНАЛЬГИН 500МГ №10 (ТЮМЕНЬ)..", "farmacy": "Аптека № 1 (Макеевка)", "price": 20, "number": 100},
        {"name": "АНАФЕРОН ДЕТСКИЙ №20 ТАБ..", "farmacy": "Аптека № 2 (Текстильщик)", "price": 200, "number": 150},
        {"name": "АНАФЕРОН ДЕТСКИЙ №20 ТАБ..", "farmacy": "Аптека №12 (Зугресс)", "price": 205, "number": 200},
        {"name": "АНАЛЬГИН 500МГ №10 (ТЮМЕНЬ)..", "farmacy": "Аптека №46 (Шахтерск)", "price": 25, "number": 300},
        {"name": "ВЕНАРУС 500МГ №60..", "farmacy": "Аптека №28 (Горловка)", "price": 152, "number": 108},
    ]

    for row in data:
        farmacy = Pharmacy.objects.get(pharmacy_name=row["farmacy"])
        product = Product.objects.get(product_name=row["name"])

        pa = ProductAvailability.objects.get_or_create(product=product, farmacy=farmacy)
        pa.number = row["number"]
        pa.save()

    # product = Product.objects.filter(product_name="АНАЛЬГИН 500МГ №10 (ТЮМЕНЬ)..", available__number__gte=2)
    product = Product.objects.filter(product_name="АНАЛЬГИН 500МГ №10 (ТЮМЕНЬ)..", available__number__gte=2)
    product.available.all()
    ProductAvailability.objects.filter(product=product)
