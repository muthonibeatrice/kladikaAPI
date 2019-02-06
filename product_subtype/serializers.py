from rest_framework import serializers
from .models import ProductSubType

class ProductSubTypeSerializer(serializers.ModelSerializer):
	
	class Meta:
		
	        model = ProductSubType
	        fields = ('subtypes')