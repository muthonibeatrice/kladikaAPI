from .models import ProductStock
from product_stock.serializers import ProductStockSerializer
from rest_framework import generics



# Create your views here.

class ProductStockList(generics.ListCreateAPIView):
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer
   

class UpdateProductStock(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer
