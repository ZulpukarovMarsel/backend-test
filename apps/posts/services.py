from django.db.models import Count

from .models import Post, Comment, Like

class PostService:
    @staticmethod
    def get_class_post():
        return Post.objects.all()

class CommentService:
    @staticmethod
    def get_class_comment():
        return Comment.objects.all()

    @staticmethod
    def get_class_post_comment(instance):
        return Comment.objects.filter(post=instance)

class LikesService:
    @staticmethod
    def get_class_likes():
        return Like.objects.all()

    @staticmethod
    def get_class_post_like(instance):
        return Like.objects.filter(post=instance)

