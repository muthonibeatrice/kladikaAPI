from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.ModelSerializer):
	
	class Meta:
		
	        model = Store
	        fields = ('merchantid','storename','email','location','phonenumber')