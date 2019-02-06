from .models import Payment
from payment.serializers import PaymentSerializer
from rest_framework import generics



# Create your views here.

class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
   

class UpdatePayment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
