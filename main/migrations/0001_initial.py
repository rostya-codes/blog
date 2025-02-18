# Generated by Django 5.1.6 on 2025-02-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New post', max_length=255, verbose_name='Title')),
                ('content', models.TextField(default='Post text', verbose_name='Text')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts_images', verbose_name='Image')),
                ('created_at', models.TimeField(auto_now_add=True, verbose_name='Upload time')),
                ('updated_at', models.TimeField(auto_now=True, verbose_name='Update time')),
            ],
        ),
    ]
