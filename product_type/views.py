from .models import ProductType
from product_type.serializers import ProductTypeSerializer
from rest_framework import generics



# Create your views here.

class ProductTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
   

class UpdateProductType(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
