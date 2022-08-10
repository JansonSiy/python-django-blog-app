from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from .forms import NewPostForm, EditPostForm

from .models import Post


def post_list(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    pagination = Paginator(post_list, 5)
    page = request.GET.get('page')
    posts = pagination.get_page(page)

    context = {
        'post_list': post_list,
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
        return redirect('post_details', post.id)

    context = {
        'form': form,
    }

    return render(request, 'blog/new_post.html', context)


def edit_post(request, id: int):
    post = get_object_or_404(Post, id=id)
    form = EditPostForm(request.POST, instance=post)

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        messages.success(request, f'{post.title} has been successfully updated!')
        return redirect('post_details', post.id)

    context = {
        'form': form,
    }

    return render(request, 'blog/edit_post.html', context)


def delete_post(request, id: int):
    post = get_object_or_404(Post, id=id)
    messages.success(request, f'{post.title} has been successfully deleted!')
    post.delete()
    return redirect(post_list)
