from django_filters import FilterSet
from .models import Post


class PostsFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'created': ['gt'],
            'title': ['contains'],
            'author__user__username': ['contains'],
        }