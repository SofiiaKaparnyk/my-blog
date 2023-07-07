from django.urls import path

from reviews import views

urlpatterns = [
    path("reviews/", views.ReviewView.as_view()),
    path("all-reviews/", views.ReviewListView.as_view()),
    path("reviews/<int:pk>", views.ReviewDetailView.as_view(), name="detail-review"),
    path("thank-you/<str:username>", views.ThankYouView.as_view(), name="thank-you"),
]
