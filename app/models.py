from django.db import models


class Farmacy(models.Model):
    """Модель торговой точки"""

    pharmacy_name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    house = models.CharField(max_length=50)
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
    product_name = models.CharField(max_length=250)
    product_manufacturer = models.CharField(max_length=250, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)


class ProductAvailability(models.Model):
    """Модель наличие товара"""

    class Meta:
        db_table = 'product_availability'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    farmacy = models.ForeignKey(Farmacy, on_delete=models.CASCADE)
    number = models.FloatField(null=True, blank=True)


# Create your models here.
