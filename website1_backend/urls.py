from django.contrib import admin
from django.urls import path
from api.views import PostListCreateView, UserListCreatView, CommentCreateView, CommentListView

urlpatterns = [
    path('admin', admin.site.urls),
    path('api/v1/posts/', PostListCreateView.as_view(), name="post-list-create-view"),
    path('api/v1/comments/', CommentCreateView.as_view(), name="comment-list-create-view"),
    path('api/v1/comments/<int:post_id>', CommentListView.as_view(), name="comment-list-create-view"),
    path('api/v1/users/', UserListCreatView.as_view(), name="user-list-create-view")
]