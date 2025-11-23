from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Post, Category, Tag , Comment

from .forms import PostForm, RegisterForm, CommentForm

from django.db.models import Q
from datetime import datetime


# Create your views here.


def home(request):
    posts = Post.objects.filter(
        status=Post.Status.PUBLISHED
    ).select_related('author', 'category').prefetch_related('tags')

    featured_posts = Post.objects.filter(
        status=Post.Status.PUBLISHED,
        is_featured=True
    )[:4]

    all_categories = [post.category.name for post in posts]

    unique_categories = list(set(all_categories))[:6]
    context = {
        'site_name': 'BlogHub',
        'tagline': 'Your Platform for Sharing Ideas',
        'total_posts': len(posts),
        'total_authors': len(set(post.author for post in posts)),
        'current_year': datetime.now().year,
        'featured_topics': unique_categories,
        'features': [
            {'icon': '✍️', 'title': 'Easy Publishing',
             'description': 'Write and publish posts effortlessly'},
            {'icon': '🎨', 'title': 'Beautiful Design',
             'description': 'Professional templates for your content'},
            {'icon': '👥', 'title': 'Engage Readers',
             'description': 'Build your audience and community'},
            {'icon': '�', 'title': 'Analytics',
             'description': 'Track your post performance'},
        ],
        'is_featured_active': True,
        'spotlight_topic': 'Web Development',
        'featured_posts': featured_posts,
    }

    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'current_year': datetime.now().year,
        'company_name': 'BlogHub Team',
        'founded_year': 2025,
        'mission': 'Empowering writers to share their stories with the world',
        'team_size': 1,
        'values': ['Creativity', 'Community', 'Quality Content', 'Freedom of Expression'],
    }

    return render(request, 'blog/about.html', context)


def posts(request):
    posts_queryset = Post.objects.filter(
        status=Post.Status.PUBLISHED
    ).select_related('author', 'category').prefetch_related('tags').order_by('-created_at')

    # Pagination
    paginator = Paginator(posts_queryset, 9)  # Show 10 posts per page
    page_number = request.GET.get('page')  # /posts/?page=2
    posts = paginator.get_page(page_number)

    context = {
        'page_title': 'All Blog Posts',
        'current_year': datetime.now().year,
        'posts': posts,
        'total_posts': posts_queryset.count(),
    }

    return render(request, 'blog/posts.html', context)


@login_required(login_url='/login/')
def post_create(request):
    """Create a new post"""
    if request.method == 'POST':
        # Form submitted
        form = PostForm(request.POST)
        if form.is_valid():
            # Save but don't commit to database yet
            post = form.save(commit=False)
            # Set the author to current user
            post.author = request.user
            # Now save to database
            post.save()
            # Save many-to-many relationships (tags)
            form.save_m2m()

            new_cat = form.cleaned_data.get('new_category')
            if new_cat:
                category_obj, _ = Category.objects.get_or_create(name=new_cat)
                post.category = category_obj
                post.save()

            new_tags = form.cleaned_data.get('new_tags')
            if new_tags:
                tag_names = [t.strip() for t in new_tags.split(',')]
                for name in tag_names:
                    tag_obj, _ = Tag.objects.get_or_create(name=name)
                    post.tags.add(tag_obj)

            # Show success message
            messages.success(request, 'Post created successfully!')
            # Redirect to the post detail page
            return redirect('blog:post_detail', slug=post.slug)
        else:
            # Form has errors
            messages.error(request, 'Please correct the errors below.')
    else:
        # GET request - show empty form
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'blog/post_form.html', context)


@login_required(login_url='/login/')
def post_update(request, slug):
    """Update an existing post"""
    # Get the post
    post = get_object_or_404(Post, slug=slug)

    # Check if user is the author
    if post.author != request.user:
        messages.error(request, 'You can only edit your own posts!')
        return redirect('blog:post_detail', slug=post.slug)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('blog:post_detail', slug=post.slug)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'blog/post_form.html', context)


@login_required(login_url='/login/')
def post_delete(request, slug):
    """Delete a post"""
    post = get_object_or_404(Post, slug=slug)

    # Check if user is the author
    if post.author != request.user:
        messages.error(request, 'You can only delete your own posts!')
        return redirect('blog:post_detail', slug=post.slug)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('blog:posts')

    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_detail(request, slug):
    post = get_object_or_404(
        Post.objects.select_related('author', 'category').prefetch_related('tags'),
        slug=slug,
    )

    post.views_count += 1
    post.save(update_fields=['views_count'])

    related_posts = Post.objects.filter(
        category=post.category,
        status=Post.Status.PUBLISHED
    ).exclude(id=post.id)[:3]

    comments = post.comments.filter(is_approved=True)

    comment_form = CommentForm()

    context = {
        'post': post,
        'related_posts': related_posts,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required(login_url='/login/')
def add_comment(request, slug):
    """Add a comment to a post"""
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
        else:
            messages.error(request, 'Error adding comment. Please try again.')

    return redirect('blog:post_detail', slug=slug)


@login_required(login_url='/login/')
def delete_comment(request, comment_id):
    """Delete a comment"""
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    slug = comment.post.slug

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')

    return redirect('blog:post_detail', slug=slug)


def category_posts(request, category_name):
    """
    Display posts filtered by category

    URL: /category/technology/
    Shows only posts in that category
    """
    posts_queryset = Post.objects.filter(
        status=Post.Status.PUBLISHED,
        category__name__iexact=category_name

    ).select_related('author', 'category').prefetch_related('tags').order_by('-created_at')

    paginator = Paginator(posts_queryset, 9)  # Show 10 posts per page
    page_number = request.GET.get('page')  # /posts/?page=2
    posts = paginator.get_page(page_number)

    context = {
        'category_name': category_name.title(),
        'posts': posts,
        'post_count': paginator.count,

    }
    return render(request, 'blog/category_posts.html', context)


def search_posts(request):
    """
    Search posts by title or content or category

    URL: /search/?q=django
    """

    posts = Post.objects.filter(
        status=Post.Status.PUBLISHED
    ).select_related('author', 'category').prefetch_related('tags')
    # Get a search query from URL parameters
    query = request.GET.get('search', '')  # Default to empty string if no query

    if query:
        search_results = posts.filter(
            Q(title__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(category__name__icontains=query) |
            Q(author__username__icontains=query)
        )
    else:
        search_results = posts

    paginator = Paginator(search_results, 9)  # Show 10 posts per page
    page_number = request.GET.get('page')  # /posts/?page=2
    posts = paginator.get_page(page_number)

    context = {
        'query': query,
        'posts': posts,
        'total_results': paginator.count,
    }
    return render(request, 'blog/search_results.html', context)


def contact(request):
    """
    Contact page with form submission
    GET: Show form
    POST: Process form submission
    """
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Basic validation
        if not all([name, email, subject, message]):
            messages.error(request, 'Please fill in all fields.')
        elif '@' not in email:
            messages.error(request, 'Please enter a valid email address.')
        else:

            print(f"Contact form submission:")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Subject: {subject}")
            print(f"Message: {message}")

            # Success message
            messages.success(request, f'Thank you {name}! We received your message and will respond soon.')

            return redirect('blog:contact')

        # GET request or after POST redirect

    context = {
        'current_year': datetime.now().year,
        'email': 'contact@bloghub.com',
        'phone': '+1-800-BLOG HUB',
        'address': '456 Writers Lane, Content City, CC 54321',
        'business_hours': 'Monday - Friday: 9AM - 6PM',
        'departments': [
            {'name': 'IT', 'email': 'it@bloghub.com'},
            {'name': 'HR', 'email': 'HR@bloghub.com'},
            {'name': 'Finance', 'email': 'Finance@bloghub.com'},
            {'name': 'Marketing', 'email': 'Marketing@bloghub.com'},
        ],

        'social_media': [
            {'platform': 'Facebook', 'url': 'https://www.facebook.com'},
            {'platform': 'Reddit', 'url': 'https://www.reddit.com'},
            {'platform': 'Twitter', 'url': 'https://www.twitter.com'},
        ]
    }
    return render(request, 'blog/contact.html', context)


def author_posts(request, author_name):
    posts = Post.objects.filter(
        status=Post.Status.PUBLISHED
    ).select_related('author', 'category').prefetch_related('tags')

    author_name_normalized = author_name.lower().replace(' ', '-')

    filtered = posts.filter(
        author__username__iexact=author_name.replace('-', ' ')
    )
    context = {
        'author_name': author_name.replace('-', ' ').title(),
        'posts': filtered,
        'total_posts': len(filtered),
        'current_year': datetime.now().year,
    }

    return render(request, 'blog/author_posts.html', context)


class MyPostsView(LoginRequiredMixin, ListView):
    """Display only the current user's posts"""
    model = Post
    template_name = 'blog/my_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class DraftPostsView(LoginRequiredMixin, ListView):
    """Display only draft posts of current user"""
    model = Post
    template_name = 'blog/draft_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user,
            status=Post.Status.DRAFT
        )


class LoginView(DjangoLoginView):
    template_name = 'blog/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('blog:home')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid email or password')
        return super().form_invalid(form)


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('blog:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully! You can now log in')
        return response

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog:home')
        return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('blog:home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You have been logged out successfully')
        return super().dispatch(request, *args, **kwargs)
