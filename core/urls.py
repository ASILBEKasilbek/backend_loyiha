from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from apps.common.views import *
from .schema import swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.common.api')),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
