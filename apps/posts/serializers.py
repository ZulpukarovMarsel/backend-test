from rest_framework import serializers
from .models import Post, Comment, Like
from apps.user.serializers import UserSerializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Like
        fields = '__all__'
