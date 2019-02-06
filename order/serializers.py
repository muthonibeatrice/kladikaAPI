from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

	class Meta:
		
	        model = Order
	        fields = ( 'ordername', 'payment_status')
	        extra_kwargs={
	        	'total':{'read-only':True},
	        }