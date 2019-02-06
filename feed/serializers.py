from rest_framework import serializers
from .models import Feed

class FeedSerializer(serializers.ModelSerializer):
	"""docstring for PhotosSerializer"""
	class Meta:
		
	        model = Feed
	        fields = ('uphoto', 'caption', 'userid', 'ordered_productsid')