from django.shortcuts import render, redirect
from .models import Post
# Create your views here.
def new(request):
    return render(request, 'pages/new.html')

def create(request):
    context = {
        'title': request.GET.get('title'),
        'content': request.GET.get('content'),
        'image_url': request.GET.get('image_url'),
    }
    Post(**context).save()
    return redirect('pages:pages')

def pages(request):
    posts = Post.objects.all()
    context = {
        'post': posts,
    }
    return render(request,'pages/index.html', context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'pages/detail.html', context)

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('pages:pages')

def update(request, pk):
    post = Post.objects.get(pk=pk)
    post.title = request.GET.get('title')
    post.content = request.GET.get('content')
    post.image_url = request.GET.get('image_url')
    post.save()
    return redirect('pages:pages')


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'pages/edit.html', context)