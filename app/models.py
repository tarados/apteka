from django.db import models


class Farmacy(models.Model):
    """Модель торговой точки"""

    pharmacy_name = models.CharField(max_length=255)
    city = models.CharField(max_length=50, null=True)
    house = models.TextField(null=True)
    street = models.CharField(null=True, max_length=50)
    state_province = models.CharField(max_length=50, null=True)
    manager = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


class Product(models.Model):
    """Модель прайс"""

    product_name = models.CharField(max_length=250, db_index=True)
    product_manufacturer = models.CharField(max_length=250, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    product_photo = models.ImageField(upload_to='images', null=True, blank=True)


class Customer(models.Model):
    """Модель заказчик"""

    customer_name = models.CharField(max_length=12)
    customer_surname = models.CharField(max_length=20)
    customer_phone = models.CharField(max_length=20)


class Order(models.Model):
    """Реестр заказов"""

    registry_customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    registry_total_price = models.FloatField(null=True, blank=True)
    registry_date = models.DateTimeField(null=True, blank=True)


class OrderItem(models.Model):
    """Модель заказ"""

    order_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order_price = models.FloatField(null=True, blank=True)
    order_quantity = models.FloatField(null=True, blank=True)
    order_cost_product = models.FloatField(null=True, blank=True)
    order_pharmacy = models.ForeignKey(Farmacy, on_delete=models.CASCADE, null=True, blank=True)


class ProductAvailability(models.Model):
    """Модель наличие товара"""

    class Meta:
        db_table = 'product_availability'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="available")
    farmacy = models.ForeignKey(Farmacy, on_delete=models.CASCADE)
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
        farmacy = Farmacy.objects.get(pharmacy_name=row["farmacy"])
        product = Product.objects.get(product_name=row["name"])

        pa = ProductAvailability.objects.get_or_create(product=product, farmacy=farmacy)
        pa.number = row["number"]
        pa.save()

    # product = Product.objects.filter(product_name="АНАЛЬГИН 500МГ №10 (ТЮМЕНЬ)..", available__number__gte=2)
    product = Product.objects.filter(product_name="АНАЛЬГИН 500МГ №10 (ТЮМЕНЬ)..", available__number__gte=2)
    product.available.all()
    ProductAvailability.objects.filter(product=product)
