from django.shortcuts import redirect, render, reverse
from django.views import View
from django.views.generic import ListView

from blog.forms import CommentForm
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


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        form = CommentForm()
        return render(
            request, "blog/post-detail.html", {"comment_form": form, "post": post}
        )

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(reverse("post-detail", args=[slug]))
        return render(
            request, "blog/post-detail.html", {"comment_form": form, "post": post}
        )
