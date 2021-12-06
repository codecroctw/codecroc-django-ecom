from django.urls import path, reverse, reverse_lazy
from django.conf.urls import url
from django.views.generic.base import TemplateView, RedirectView

from .views import product_detail_view, product_list_view

app_name = 'shop'

urlpatterns = [
    #path('product/<int:id>', product_detail_view, name='product-detail'),
    path('products/', product_list_view, name='product-list'),
    url(r'^product/(?P<id>\d+)/$', product_detail_view, name='product-detail'),
    path('template-view', TemplateView.as_view(template_name='shop/template-view.html'),
         name='template-view'),
    path('redirect-view', RedirectView.as_view(url=reverse_lazy('shop:template-view')),
         name='redirect-view')
]
