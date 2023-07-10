from django.views.generic import DetailView, ListView

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


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        context["comment_form"] = form
        return context
