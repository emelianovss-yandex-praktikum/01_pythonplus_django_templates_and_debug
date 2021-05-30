from django.contrib.auth import get_user_model
from django.shortcuts import render

from posts.models import Post

User = get_user_model()


def index(request):
    post = Post.objects.first()
    if post:
        context = {
            'title': post.title,
            'username': post.user.username,
            'email': post.user.email
        }
    else:
        context = {}
    return render(request, 'index.html', context)


def posts(request):
    context = {
        # 'objects': Post.objects.prefetch_related('user').all()
        # 'objects': Post.objects.select_related('user').all()
        'objects': Post.objects.all()
    }
    return render(request, 'posts/index.html', context)


def users(request):
    context = {
        'title': 'Список пользователей',
        'objects': User.objects.all()
    }
    return render(request, 'posts/user_list.html', context)
