from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.admin import shop_admin

from shop.views import (home, post_view, product_detail_view,
                        test2, http_response, redirect_view)

urlpatterns = [
    path('', home),
    path('auth/', include('django.contrib.auth.urls')),
    path('test2/', test2),
    path('http_response/', http_response),
    path('post/', post_view),
    path('product-detail', product_detail_view),
    path('redirect/', redirect_view),
    path('admin/', admin.site.urls),
    path('shop_admin/', shop_admin.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.index_title = 'Django Ecom 後台'
admin.site.site_header = 'CodeCroc 管理'
admin.site.site_title = 'CodeCroc Ecom'
