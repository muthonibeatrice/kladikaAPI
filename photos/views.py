from .models import Photos
from photos.serializers import PhotosSerializer
from rest_framework import generics



# Create your views here.

class PhotosList(generics.ListCreateAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
   

class UpdatePhotos(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer# -*- coding: utf-8 -*-

# Create your views here.
