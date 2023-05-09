from django.db import models


class Post(models.Model):
    slug = models.SlugField(unique=True)
    img = models.CharField()
    author = models.CharField()
    date = models.TimeField(auto_now_add=True)
    title = models.CharField()
    excerpt = models.CharField()
    content = models.CharField()
