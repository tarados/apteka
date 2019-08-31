from django.db import models


class Farmacy(models.Model):
    """Модель торговой точки"""

    pharmacy_name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    house = models.TextField()
    street = models.CharField(null=True, max_length=50)
    state_province = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


class Product(models.Model):
    """Модель прайс"""

    class Meta:
        db_table = 'product'

    # product_id = models.IntegerField()
    product_name = models.CharField(max_length=250, db_index=True)
    product_manufacturer = models.CharField(max_length=250, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)


class ProductAvailability(models.Model):
    """Модель наличие товара"""

    class Meta:
        db_table = 'product_availability'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="available")
    farmacy = models.ForeignKey(Farmacy, on_delete=models.CASCADE)
    number = models.FloatField(null=True, blank=True)


def test():
    data = [
        {"name": "Анальгин", "farmacy": "Харцизк1", "price": 20, "number": 100},
        {"name": "Аспирин", "farmacy": "Харцизк1", "price": 20, "number": 100},
        {"name": "Анальгин", "farmacy": "Харцизк2", "price": 20, "number": 100},
        {"name": "Анальгин", "farmacy": "Харцизк3", "price": 20, "number": 100},
        {"name": "Анальгин", "farmacy": "Харцизк4", "price": 20, "number": 100},
    ]

    for row in data:
        farmacy = Farmacy.objects.get(pharmacy_name=row["farmacy"])
        product = Product.objects.get(product_name=row["name"])

        pa = ProductAvailability.objects.get_or_create(product=product, farmacy=farmacy)
        pa.number = row["number"]
        pa.save()

    product = Product.objects.filter(product_name="Анальгин", available__number__gte=2)
    product = Product.objects.filter(product_name="Анальгин", available__number__gte=2)
    product.available.all()
    ProductAvailability.objects.filter(product=product)
