from django.shortcuts import render

from blog.models import Post


def index(request):
    posts = Post.objects.order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": posts})


def all_posts(request):
    posts = Post.objects.order_by("-date")
    return render(request, "blog/all_posts.html", {"posts": posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})
