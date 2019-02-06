from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
	"""docstring for MerchantSerializer"""
	class Meta:
		
	        model = Products
	        fields = ("__all__")
			