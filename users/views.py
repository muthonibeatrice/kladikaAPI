from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import MyUser
from users.serializers import UserSerializer
from rest_framework import generics,permissions
from rest_framework.generics import CreateAPIView
#from django.contrib.auth import get_user_model



# Create your views here.

class UserList(generics.ListCreateAPIView):
	#permission_classes = (IsAuthenticated,) #Only Authenticated users perform CRUD Operations
	queryset = MyUser.objects.all()
	serializer_class = UserSerializer
   

class UpdateUser(generics.RetrieveUpdateDestroyAPIView):
	queryset = MyUser.objects.all()
	serializer_class = UserSerializer

