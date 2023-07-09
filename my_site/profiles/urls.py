from django.urls import path

from . import views
from .views import ProfilesView

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("user-profiles/", ProfilesView.as_view()),
]
