from .models import Feed
from feed.serializers import FeedSerializer
from rest_framework import generics



# Create your views here.

class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
   

class UpdateFeed(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer