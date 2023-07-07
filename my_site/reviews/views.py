from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView

from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse("thank-you", kwargs={"username": form.cleaned_data["username"]})
            )
        return render(request, "reviews/review.html", {"form": form})


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"name": kwargs["username"]})
        return context
