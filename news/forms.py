from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'post_type', 'cats', 'title', 'text', 'rating']