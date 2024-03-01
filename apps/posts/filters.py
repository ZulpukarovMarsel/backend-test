import django_filters
from django.db.models import Subquery, OuterRef, Count

from apps.posts.models import Post, Like

class PostFilter(django_filters.FilterSet):
    min_likes = django_filters.NumberFilter(method='filter_min_likes', label='Min Likes')
    max_likes = django_filters.NumberFilter(method='filter_max_likes', label='Max Likes')

    class Meta:
        model = Post
        fields = ['created_at', 'author']

    def filter_min_likes(self, queryset, name, value):
        return queryset.annotate(likes_count=Count('like')).filter(likes_count__gte=value)

    def filter_max_likes(self, queryset, name, value):
        return queryset.annotate(likes_count=Count('like')).filter(likes_count__lte=value)

    def filter_created_at(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(created_at__date=value)

    def filter_author(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(author__username=value)