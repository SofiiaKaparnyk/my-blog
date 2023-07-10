from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.base import TemplateView, View

from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse(
            "thank-you", kwargs={"username": self.request.POST.get("username")}
        )


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#
#     def get_success_url(self):
#         """Return the URL to redirect to after processing a valid form."""
#         return reverse("thank-you", kwargs={"username": self.request.POST.get("username")})
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_favorite"] = (
            int(self.request.session.get("favorite_review")) == self.object.pk
        )
        return context


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"name": kwargs["username"]})
        return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return redirect(reverse("detail-review", kwargs={"pk": review_id}))
