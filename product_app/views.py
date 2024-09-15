from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewset(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['category']  # Filtering by category
    search_fields = ['name']  # Searching by name
    ordering_fields = ['price']  # Ordering by price
