from rest_framework import generics
from rest_framework.response import Response
from .models import Posts
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer