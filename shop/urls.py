from django.urls import path
from .views import product_detail_view

app_name = 'shop'

urlpatterns = [

    path('product/<int:id>', product_detail_view, name='product-detail'),
]
