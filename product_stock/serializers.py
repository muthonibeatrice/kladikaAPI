from rest_framework import serializers
from .models import ProductStock

class ProductStockSerializer(serializers.ModelSerializer):

	class Meta:
		
	        model = ProductStock
	        fields = ( 'Quantity', 'productid', 'product_variantid')
			