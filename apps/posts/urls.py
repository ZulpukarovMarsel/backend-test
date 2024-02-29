from django.urls import path
from .views import PostListView, PostDetailView, CommentListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-api'),
    path('post/<int:id>/', PostDetailView.as_view(), name='post-detail-api'),
    path('comments/', CommentListView.as_view(), name='comments-api'),
]
