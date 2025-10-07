from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet

# Create DRF router and register ProductViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

# Include router URLs
urlpatterns = [
    path('', include(router.urls)),
]
