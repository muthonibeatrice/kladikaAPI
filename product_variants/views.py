# -*- coding: utf-8 -*-
from .models import ProductVariants
from product_variants.serializers import ProductVariantsSerializer
from rest_framework import generics



# Create your views here.

class ProductVariantsList(generics.ListCreateAPIView):
    queryset = ProductVariants.objects.all()
    serializer_class = ProductVariantsSerializer
   

class UpdateProductVariants(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductVariants.objects.all()
    serializer_class = ProductVariantsSerializer
    