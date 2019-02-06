from .models import Store
from store.serializers import StoreSerializer
from rest_framework import generics



# Create your views here.

class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
   

class UpdateStore(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer