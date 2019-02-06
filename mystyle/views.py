from .models import MyStyle
from mystyle.serializers import MyStyleSerializer
from rest_framework import generics



# Create your views here.

class MyStyleList(generics.ListCreateAPIView):
    queryset = MyStyle.objects.all()
    serializer_class = MyStyleSerializer
   

class UpdateMyStyle(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyStyle.objects.all()
    serializer_class = MyStyleSerializer
