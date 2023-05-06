from datetime import date

from django.shortcuts import render

# Create your views here.

posts = [
    {
        "slug": "hiking",
        "img": "mountain.jpg",
        "author": "Sofiia",
        "date": date(2023, 5, 7),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get whilst travelling!",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore 
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id 
        est laborum.
        """,
    },
    {
        "slug": "swimming",
        "img": "ocean-waves.jpg",
        "author": "Sofiia",
        "date": date(2023, 3, 7),
        "title": "Swimming in the ocean!",
        "excerpt": "There's nothing like the views you get whilst travelling!",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore 
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id 
        est laborum.
        """,
    },
    {
        "slug": "hiking",
        "img": "mountain.jpg",
        "author": "Sofiia",
        "date": date(2023, 5, 7),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get whilst travelling!",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore 
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id 
        est laborum.
        """,
    },
    {
        "slug": "swimming",
        "img": "ocean-waves.jpg",
        "author": "Sofiia",
        "date": date(2023, 3, 7),
        "title": "Swimming in the ocean!",
        "excerpt": "There's nothing like the views you get whilst travelling!",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore 
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id 
        est laborum.
        """,
    },
]


def index(request):
    sorted_posts = sorted(posts, key=lambda p: p.get("date"), reverse=True)
    return render(request, "blog/index.html", {"posts": sorted_posts[:3]})


def all_posts(request):
    return render(request, "blog/all_posts.html", {"posts": posts})


def post_detail(request, slug):
    post = next(post for post in posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": post})
