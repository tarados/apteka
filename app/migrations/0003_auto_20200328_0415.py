# Generated by Django 2.2.10 on 2020-03-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200327_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Новый'), (2, 'В обработке'), (3, 'Выполнен')], default=1, verbose_name='Статус'),
        ),
    ]
