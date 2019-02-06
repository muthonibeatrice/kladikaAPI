# -*- coding: utf-8 -*-
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .models import Merchant
from merchant.serializers import MerchantSerializer
from rest_framework import generics, permissions,pagination,filters



# Create your views here.

class MerchantList(generics.ListCreateAPIView):
	queryset = Merchant.objects.all()
	serializer_class = MerchantSerializer
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	filter_backends = (filters.OrderingFilter,)
	#ordering_fields = ('storename', 'speciality')
	#ordering = ('speciality',)
	#filter_fields = ('speciality', 'location')

	#def get_queryset(self):
	
	#To determine the initial queryset based on query parameters in the url.
		
		#username = self.request.query_params.get('username', None)
		#if username is not None:
			#queryset = queryset.filter(storename=username)
		#return queryset
   

class UpdateMerchant(generics.RetrieveUpdateDestroyAPIView):
	#queryset = Merchant.objects.all()
	serializer_class = MerchantSerializer


	def get_queryset(self):

			 username = self.kwargs['username']
			 return Merchant.objects.filter(storename=username) #filter against current user.

		
	
