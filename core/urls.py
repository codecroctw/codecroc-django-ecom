from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.index_title = 'Django Ecom 後台'
admin.site.site_header = 'CodeCroc 管理'
admin.site.site_title = 'CodeCroc Ecom'
