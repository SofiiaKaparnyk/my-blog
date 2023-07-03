from django.contrib import admin

from blog.models import Author, Post, Tag

admin.site.register(Tag)
admin.site.register(Author)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "author", "date")
    prepopulated_fields = {"slug": ("title",)}
