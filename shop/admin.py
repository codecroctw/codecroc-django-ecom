from django.contrib import admin

from .models import Product, Category, Order, Mapping

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Mapping)


class ShopAdminSite(admin.AdminSite):
    site_header = '商品後台'
    index_title = '商品後台'


shop_admin = ShopAdminSite(name='ShopAdmin')
shop_admin.register(Product)
shop_admin.register(Category)
shop_admin.register(Order)