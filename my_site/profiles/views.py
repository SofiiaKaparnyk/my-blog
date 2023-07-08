from django.shortcuts import redirect, render
from django.views import View


def store_file(file):
    with open(f"temp/{file.name}", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        file = request.FILES["image"]
        store_file(file)
        return redirect("/profiles")
