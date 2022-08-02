from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from .forms import NewPostForm

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


def new_post(request):
    form = NewPostForm(request.POST)

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        messages.success(request, 'post has been created!')
        return redirect('post_list')
    else:
        form = NewPostForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/new_post.html', context)
