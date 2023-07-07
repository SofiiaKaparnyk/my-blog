from django.urls import path

from reviews import views

urlpatterns = [
    path("reviews/", views.ReviewView.as_view()),
    path("thank-you/<str:username>", views.thank_you, name="thank-you"),
]
