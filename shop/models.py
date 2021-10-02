from django.db import models
from uuid import uuid4
from django.utils import timezone


def path_and_rename(instance, filename):
    ext = filename.split('.')[-1]
    now = timezone.now()
    return f"{now.year}/{now.month}/{now.day}/{uuid4().hex}.{ext}"


class Category(models.Model):
    title = models.CharField('標題', max_length=63)
    image = models.ImageField(
        '圖片', null=True, default=None, upload_to=path_and_rename)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '產品類別'
        verbose_name_plural = '產品類別'


class Product(models.Model):
    title = models.CharField('標題', max_length=127)
    description = models.TextField('描述', blank=True, null=True)
    primary_image = models.ImageField(
        '主要圖片', null=True, default=None, upload_to=path_and_rename)
    original_price = models.DecimalField(
        '原價', max_digits=6, decimal_places=2, default=0.00)
    discounted_price = models.DecimalField(
        '特價', max_digits=6, decimal_places=2, default=0.00)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='產品類別')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '產品'
        verbose_name_plural = '產品'
