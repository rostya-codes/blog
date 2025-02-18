from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from main.models import Post


# Список постов
class PostListView(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'

# Детальный просмотр поста
class PostDetailView(DetailView):
    model = Post
    template_name = 'main/landing.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

# Создание поста
class PostCreateView(CreateView):
    model = Post
    template_name = 'main/post_form.html'
    fields = ('title', 'content')
    success_url = reverse_lazy('main:index')  # После создания поста перенаправление на список

# Редактирование поста
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'main/post_form.html'
    fields = ('title', 'content')
    success_url = reverse_lazy('main:index')

# Удаление поста
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'main/post_confirm_delete.html'
    success_url = reverse_lazy('main:index')  # Перенаправление после удаления
