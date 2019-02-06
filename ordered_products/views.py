# -*- coding: utf-8 -*-
from .models import OrderedProducts
from ordered_products.serializers import OrderedProductsSerializer
from rest_framework import generics



# Create your views here.

class OrderedProductsList(generics.ListCreateAPIView):
    queryset = OrderedProducts.objects.all()
    serializer_class = OrderedProductsSerializer
   

class UpdateOrderedProducts(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderedProducts.objects.all()
    serializer_class = OrderedProductsSerializer
    