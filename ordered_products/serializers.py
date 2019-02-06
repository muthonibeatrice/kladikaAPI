from rest_framework import serializers
from .models import OrderedProducts

class OrderedProductsSerializer(serializers.ModelSerializer):
	
	class Meta:
		
	        model = OrderedProducts
	        fields = ('productsid','orderid','userid')
			

	        extra_kwargs={
	        	'quantity':{'read-only':True},
	        	'amount':{'read-only':True},
	        }