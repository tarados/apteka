# Generated by Django 2.2.6 on 2020-02-09 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_product_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=12)),
                ('customer_surname', models.CharField(max_length=20)),
                ('customer_phone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('order_quantity_product', models.FloatField()),
                ('order_value_product', models.FloatField()),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registry_total_price', models.FloatField()),
                ('registry_date', models.DateField()),
                ('registry_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
                ('registry_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Order')),
            ],
            options={
                'db_table': 'registry',
            },
        ),
    ]