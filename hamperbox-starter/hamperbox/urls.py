from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from shop.views import home  # import view directly
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls')),  # DRF endpoints
    path('', home),  # Root URL serves the storefront homepage
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)