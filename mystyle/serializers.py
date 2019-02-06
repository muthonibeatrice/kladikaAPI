from rest_framework import serializers
from .models import MyStyle

class MyStyleSerializer(serializers.ModelSerializer):
	"""docstring for MyStyleSerializer"""
	class Meta:
		
	        model = MyStyle
	        fields = ('userid', 'productid')
			