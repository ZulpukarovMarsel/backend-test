from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .pagination import Pagination
from .services import PostService, CommentService, LikesService
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter

class PostListView(generics.ListCreateAPIView):
    queryset = PostService.get_class_post()
    serializer_class = PostSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
    permission_classes = []

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Не удалось получить сообщения. {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PostDetailView(generics.RetrieveAPIView):
    queryset = PostService.get_class_post()
    serializer_class = PostSerializer
    permission_classes = []
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        try:
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
        except PostService.get_class_post().DoesNotExist:
            return Response({"error": "Пост не найдено"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"Не удалось получить сведения о публикации. {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class CommentListView(generics.ListCreateAPIView):
    queryset = CommentService.get_class_comment()
    serializer_class = CommentSerializer
    pagination_class = Pagination
    permission_classes = []

class LikeListView(generics.ListCreateAPIView):
    queryset = LikesService.get_class_likes()
    serializer_class = LikeSerializer
    permission_classes = []
