from django.urls import path
from .views import PostListView, PostDetailView, CommentListView, LikeListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-api'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post-detail-api'),
    path('comments/', CommentListView.as_view(), name='comments-api'),
    path('likes/', LikeListView.as_view(), name='likes-api')
]
