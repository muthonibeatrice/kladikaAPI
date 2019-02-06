from rest_framework import serializers
from .models import Photos

class PhotosSerializer(serializers.ModelSerializer):
	"""docstring for PhotosSerializer"""
	class Meta:
		
	        model = Photos
	        fields = ('id','merchantid', 'photoid', 'photos')
			