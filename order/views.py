from .models import Order
from order.serializers import OrderSerializer
from rest_framework import generics



# Create your views here.

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
   

class UpdateOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
