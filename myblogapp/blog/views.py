from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    context = {
        'posts': posts,
    }

    return render(request, 'blog/post_list.html', context)


def post_details(request, id: int):
    post = get_object_or_404(Post, id=id)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_details.html', context)