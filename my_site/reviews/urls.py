from django.urls import path

from reviews import views

urlpatterns = [
    path("reviews/", views.review),
    path("thank-you/<str:username>", views.thank_you, name="thank-you"),
]
