from rest_framework import generics
from rest_framework.response import Response
from .models import Posts, Comments, User
from .serializers import PostSerializer, CommentSerializer, UserSerializer

class UserListCreatView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class CommentCreateView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class CommentListView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comments.objects.filter(post_id=post_id)