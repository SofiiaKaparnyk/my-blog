from django.shortcuts import redirect, render
from django.urls import reverse


def review(request):
    if request.method == "POST":
        username = request.POST["name"]
        return redirect(reverse("thank-you", kwargs={"username": username}))
    return render(request, "reviews/review.html")


def thank_you(request, username):
    return render(request, "reviews/thank_you.html", {"name": username})
