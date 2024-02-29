from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .services import PostService, CommentService, LikesService
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
class PostListView(generics.ListCreateAPIView):
    queryset = PostService.get_class_post()
    serializer_class = PostSerializer
    permission_classes = []


class PostDetailView(generics.RetrieveAPIView):
    queryset = PostService.get_class_post()
    serializer_class = PostSerializer
    permission_classes = []
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        post_serializer = self.get_serializer(instance)
        comment_queryset = CommentService.get_class_post_comment(instance)
        comment_serializer = CommentSerializer(comment_queryset, many=True)
        like_queryset = LikesService.get_class_post_like(instance)
        like_serializer = LikeSerializer(like_queryset, many=True)

        data = {
            'post': post_serializer.data,
            'likes': like_serializer.data,
            'comments': comment_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)
class CommentListView(generics.ListCreateAPIView):
    queryset = CommentService.get_class_comment()
    serializer_class = CommentSerializer
    permission_classes = []

class LikeListView(generics.ListCreateAPIView):
    queryset = LikesService.get_class_likes()
    serializer_class = LikeSerializer
    permission_classes = []
