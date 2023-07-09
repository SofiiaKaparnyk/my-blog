from django.views.generic import CreateView, ListView

from profiles.models import UserProfile


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    success_url = "/profiles/"
    fields = ["image"]


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"


# class CreateProfileView(View):
#     def get(self, request):
#         form = FileUploadForm()
#         return render(request, "profiles/create_profile.html", {"form": form})
#
#     def post(self, request):
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES["image"]
#             UserProfile.objects.create(image=file)
#             return redirect("/profiles")
#         return render(request, "profiles/create_profile.html", {"form": form})
