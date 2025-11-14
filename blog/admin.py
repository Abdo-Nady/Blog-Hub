from django.contrib import admin
from unicodedata import category

from .models import Category, Tag, Post, Comment
from django.utils.html import format_html

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "post_count")
    search_fields = ("name",)
    ordering = ("name",)
    list_per_page = 20

    def post_count(self, obj):
        return obj.posts.count()

    post_count.short_description = "Used In Posts"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "published",
        "is_featured",
        "read_time",
        "views",
        "created_at",
        "colored_status",
        "tag_list",
    )
    list_filter = (
        "published",
        "is_featured",
        "category",
        "author",
        "tags",
        "created_at",
    )
    search_fields = (
        "title",
        "excerpt",
        "author__first_name",
        "author__last_name",
        "category__name",
        "tags__name",
    )
    list_per_page = 15
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ("views", "created_at")

    def tag_list(self, obj):
        tags = obj.tags.all()
        tags_list = []
        for tag in tags:
            tags_list.append(
                f"<span style='color:white;background-color:#333;padding:0 5px;border-radius:8px;'>{tag.name}</span>"
            )
        return format_html(" ".join(tags_list))

    tag_list.short_description = "Tags"

    def colored_status(self, obj):
        color = "green" if obj.published else "red"
        status = "Published" if obj.published else "Draft"
        return format_html(f'<span style="color: {color};">{status}</span>')

    colored_status.short_description = "Status"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)