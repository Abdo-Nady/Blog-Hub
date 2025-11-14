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
        "status",
        "is_featured",
        "read_time",
        "views",
        "created_at",
        "colored_status",
        "tag_list",
    )
    list_filter = (
        "status",
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

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author')
        }),
        ('Content', {
            'fields': ('excerpt', 'content')
        }),
        ('Classification', {
            'fields': ('category', 'tags')
        }),
        ('Settings', {
            'fields': ('status', 'is_featured', 'allow_comments')
        }),
        ('Metadata', {
            'fields': ('views_count', 'published_at', 'created_at'),
            'classes': ('collapse',),  # Collapsible section
        }),
    )
    filter_horizontal = ('tags',)

    readonly_fields = ("views", "created_at")


    actions = ['make_published', 'make_draft', 'reset_views']

    def make_published(self, request, queryset):
        """Publish selected posts."""
        updated = queryset.update(status=Post.Status.PUBLISHED)
        self.message_user(
            request,
            f'{updated} post(s) were successfully published.'
        )

    make_published.short_description = 'Publish selected posts'

    def make_draft(self, request, queryset):
        """Set selected posts to draft."""
        updated = queryset.update(status=Post.Status.DRAFT)
        self.message_user(
            request,
            f'{updated} post(s) were set to draft.'
        )

    make_draft.short_description = 'Set selected posts to draft'

    def reset_views(self, request, queryset):
        """Reset view count to zero."""
        updated = queryset.update(views_count=0)
        self.message_user(
            request,
            f'View count reset for {updated} post(s).',
            level='warning'
        )

    reset_views.short_description = 'Reset view count'

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
        color = "green" if obj.status == Post.Status.PUBLISHED else "red"
        status = obj.get_status_display()
        return format_html(f'<span style="color: {color};">{status}</span>')

    colored_status.short_description = "Status"



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)