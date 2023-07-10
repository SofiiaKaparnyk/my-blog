from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blog.models import Post


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]


class PostListView(ListView):
    model = Post
    template_name = "blog/all_posts.html"
    context_object_name = "posts"
    ordering = ["-date"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
