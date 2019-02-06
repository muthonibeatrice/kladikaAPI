# -*- coding: utf-8 -*-
from .models import Products
from products.serializers import ProductsSerializer
from rest_framework import generics



# Create your views here.

class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
   

class UpdateProducts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    