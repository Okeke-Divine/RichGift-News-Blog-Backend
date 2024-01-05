from rest_framework import serializers
from .models import Posts, Comments

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['post_id','post_title','post_description','post_content','url_to_image','time_created_text','net_views']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'