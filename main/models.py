from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, default='New post', verbose_name='Title')
    content = models.TextField(default='Post text', verbose_name='Text')
    image = models.ImageField(upload_to='posts_images', null=True, blank=True, verbose_name='Image')
    created_at = models.TimeField(auto_now_add=True, verbose_name='Upload time')
    updated_at = models.TimeField(auto_now=True, verbose_name='Update time')

    def __str__(self):
        return self.title
