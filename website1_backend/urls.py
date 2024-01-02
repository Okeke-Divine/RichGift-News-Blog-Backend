from django.contrib import admin
from django.urls import path
from api.views import PostListCreateView

urlpatterns = [
    path('admin', admin.site.urls),
    path('api/v1/posts/', PostListCreateView.as_view(), name="post-list-create-view")
]