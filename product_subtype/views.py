from .models import ProductSubType
from product_subtype.serializers import ProductSubTypeSerializer
from rest_framework import generics



# Create your views here.

class ProductSubTypeList(generics.ListCreateAPIView):
    queryset = ProductSubType.objects.all()
    serializer_class = ProductSubTypeSerializer
   

class UpdateProductSubType(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductSubType.objects.all()
    serializer_class = ProductSubTypeSerializer