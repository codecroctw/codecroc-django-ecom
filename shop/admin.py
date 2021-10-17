from django.contrib import admin
from django import forms

from .models import Product, Category, Order, Mapping

# Register your models here.


@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_preview', 'test_button']
    list_display_links = ['id', 'title', 'image_preview', ]

    readonly_fields = ['image_preview', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_preview', 'category',
                    'original_price', 'discounted_price']
    search_fields = ['title', 'description', ]
    list_filter = ['category', ]
    list_display_links = ['id', 'title', 'image_preview', ]
    readonly_fields = ['image_preview', ]


class OrderProductInline(admin.TabularInline):
    model = Mapping
    extra = 1
    readonly_fields = ['subtotal', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status',
                    'created_at', 'updated_at', 'total']
    list_editable = ['status', ]
    list_filter = ['status', 'created_at', 'updated_at', ]
    search_fields = ['name', 'phone', 'admin', ]
    inlines = [OrderProductInline, ]


class ShopAdminSite(admin.AdminSite):
    site_header = '商品後台'
    index_title = '商品後台'


shop_admin = ShopAdminSite(name='ShopAdmin')
shop_admin.register(Product)
shop_admin.register(Category)
shop_admin.register(Order)
