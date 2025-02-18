from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('post/<int:post_id>', views.PostDetailView.as_view(), name='post_detail'),
    path("post/new/", views.PostCreateView.as_view(), name="post_create"),  # Создание
    path("post/<int:post_id>/edit/", views.PostUpdateView.as_view(), name="post_update"),  # Редактирование
    path("post/<int:post_id>/delete/", views.PostDeleteView.as_view(), name="post_delete"),  # Удаление
]
