from django.shortcuts import redirect, render
from django.views import View

from profiles.forms import FileUploadForm
from profiles.models import UserProfile


class CreateProfileView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["image"]
            UserProfile.objects.create(image=file)
            return redirect("/profiles")
        return render(request, "profiles/create_profile.html", {"form": form})
