# Generated by Django 3.2.7 on 2021-10-07 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20211007_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='shop.Product', verbose_name='訂單內容'),
        ),
    ]
