from rest_framework import serializers
from .models import ProductVariants

class ProductVariantsSerializer(serializers.ModelSerializer):

	class Meta:
		
	        model = ProductVariants
	        fields = ( 'size', 'color', 'material_type', 'gallery_photos')

	        extra_kwargs={
	        	'quantity':{'read-only':True},
	        }
			