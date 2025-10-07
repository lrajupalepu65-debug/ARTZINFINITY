from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_active=True).prefetch_related('images')
    serializer_class = ProductSerializer

def home(request):
    """
    Homepage view: displays all active products with their images.
    """
    products = Product.objects.filter(is_active=True).prefetch_related('images')
    return render(request, 'shop/home.html', {'products': products})



class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_active=True).prefetch_related('images')
    serializer_class = ProductSerializer