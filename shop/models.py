from django.db import models
from django.utils import timezone
from django.conf import settings

from uuid import uuid4

User = settings.AUTH_USER_MODEL  # auth.User


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


class Order(models.Model):

    class StatusChoices(models.TextChoices):
        ORDER_SENT = 'order_sent', '已下單'
        PAID = 'paid', '已付款'
        INVOICE_MADE = 'invoce_made', '已開立發票'
        PRODUCT_SENT = 'product_sent', '已寄出'
        ORDER_CLOSED = 'order_closed', '訂單結束'
        ORDER_FAILED = 'order_failed', '訂單失敗'

    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='客戶')
    created_at = models.DateTimeField('建立於', auto_now_add=True)
    updated_at = models.DateTimeField('更新於', auto_now=True)
    total = models.DecimalField(
        '特價', max_digits=6, decimal_places=2, default=0.00)
    status = models.CharField(
        '訂單狀態', max_length=63, choices=StatusChoices.choices, default=StatusChoices.ORDER_SENT)
    products = models.ManyToManyField(
        Product, verbose_name='訂單內容', related_name='orders', through='Mapping')

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = '訂單'
        verbose_name_plural = '訂單'


class Mapping(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name='訂單')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='產品')
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(
        '小計', max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"訂單編號：{self.order.id}-{self.product.title}"

    class Meta:
        verbose_name = '訂單產品'
        verbose_name_plural = '訂單產品'
