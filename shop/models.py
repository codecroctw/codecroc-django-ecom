from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=63)
    image = models.ImageField(null=True, default=None)


class Product(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField(blank=True, null=True)
    primary_image = models.ImageField(null=True, default=None)
    original_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00)
    discounted_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL)
