from django.urls import path
from .views import PostsList, PostsDetail, SearchList, PostsCreateView, PostsUpdateView, PostsDeleteView  # импортируем наше представление

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostsDetail.as_view(), name='posts_detail'),
    path('search', SearchList.as_view()),
    path('add', PostsCreateView.as_view(), name='posts_create'),
    path('<int:pk>/edit', PostsUpdateView.as_view(), name='posts_edit'),
    path('<int:pk>/delete', PostsDeleteView.as_view(), name='posts_delete'),
]