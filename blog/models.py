from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone


class Category(models.Model):
    """Blog post categories for organization."""
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text='Category name (max 100 characters)'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text='URL-friendly version of the name'
    )
    description = models.TextField(
        blank=True,
        help_text='Optional category description'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    icon = models.CharField(max_length=50, default='default-icon')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    """Flexible tags for posts."""
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text='Tag name (max 50 characters)'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text='URL-friendly version of the name'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    """Main blog post model."""

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    # Basic fields
    title = models.CharField(
        max_length=200,
        help_text='Post title (max 200 characters)'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='URL-friendly version of the title'
    )
    excerpt = models.TextField(
        blank=True,
        help_text='Optional short summary of the post'
    )
    content = models.TextField(
        help_text='Main content of the post'
    )

    read_time = models.IntegerField(
        default=5,
        help_text='Estimated time to read the post (in minutes)'
    )



    # Status and visibility
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
        help_text='Publication status'
    )
    is_featured = models.BooleanField(
        default=False,
        help_text='Feature this post on homepage'
    )
    allow_comments = models.BooleanField(
        default=True,
        help_text='Allow users to comment'
    )


    # Relationships
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='posts'
    )

    # Metadata
    views_count = models.IntegerField(
        default=0,
        help_text='Number of views'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text='Date and time when published'
    )

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', '-created_at']),
            models.Index(fields=['-published_at']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.title)

        # Set published_at when status changes to published
        if self.status == self.Status.PUBLISHED and not self.published_at:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)




class Comment(models.Model):
    """User comments on blog posts."""
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField(
        help_text='Comment content'
    )
    is_approved = models.BooleanField(
        default=False,
        help_text='Approve comment for display'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['post', '-created_at']),
        ]

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'