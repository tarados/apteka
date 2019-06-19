# Generated by Django 2.2.2 on 2019-06-15 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmacy_id', models.IntegerField()),
                ('pharmacy_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('house', models.CharField(max_length=50)),
                ('state_province', models.CharField(max_length=50)),
                ('manager', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=250)),
                ('product_manufacturer', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(blank=True, null=True)),
                ('farmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Farmacy')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
            ],
            options={
                'db_table': 'product_availability',
            },
        ),
    ]
