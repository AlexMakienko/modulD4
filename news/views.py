from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
from .filters import PostsFilter
from .forms import PostForm
from django.core.paginator import Paginator


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-created')
    paginate_by = 10
    form_class = PostForm
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostsFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class SearchList(ListView):
    model = Post
    template_name = "search.html"
    context_object_name = "news"
    queryset = Post.objects.order_by('-created')
    paginate_by = 10
    form_class = PostForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostsFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


# создаём представление, в котором будут детали конкретного отдельного товара
class PostsDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объектаject_name = "article"
    queryset = Post.objects.all()


class PostDetailView(DetailView):
    template_name = 'posts_detail.html'
    queryset = Post.objects.all()


class PostsCreateView(CreateView):
    template_name = 'posts_create.html'
    form_class = PostForm


class PostsUpdateView(UpdateView):
    template_name = 'posts_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostsDeleteView(DeleteView):
    template_name = 'posts_delete.html'
    context_object_name = "article"
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)