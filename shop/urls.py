from django.urls import path, include
from django.conf.urls import url

from .views import product_detail_view

app_name = 'shop'

urlpatterns = [
    #path('product/<int:id>', product_detail_view, name='product-detail'),
    url(r'^product/(?P<id>\d+)/$', product_detail_view, name='product-detail')
]
