from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
queryset = Product.objects.filter(is_active=True).prefetch_related('images')
serializer_class = ProductSerializer
