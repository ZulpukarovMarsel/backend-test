from django.contrib import admin
from .models import Post, Comment, Like
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['photo', 'author', 'description', 'created_at']
    list_filter = ['created_at', 'author']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'text', 'created_at']
    list_filter = ['author', 'created_at', 'post']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user']
    list_filter = ['post', 'user']
