from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from reviews.forms import ReviewForm


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


def thank_you(request, username):
    return render(request, "reviews/thank_you.html", {"name": username})
