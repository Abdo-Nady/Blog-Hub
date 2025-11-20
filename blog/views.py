from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, Category
from .forms import PostForm
from django.db.models import Q

from datetime import datetime, date


# Create your views here.


def home(request):
    posts = Post.objects.filter(
        status=Post.Status.PUBLISHED
    ).select_related('author', 'category').prefetch_related('tags')

    featured_posts = Post.objects.filter(
        status=Post.Status.PUBLISHED,
        is_featured=True
    )[:3]

    all_categories = [post.category.name for post in posts]

    unique_categories = list(set(all_categories))
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
    ).select_related('author', 'category').prefetch_related('tags')

    # Pagination
    paginator = Paginator(posts_queryset, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')  # /posts/?page=2
    posts = paginator.get_page(page_number)

    context = {
        'page_title': 'All Blog Posts',
        'current_year': datetime.now().year,
        'posts': posts,
        'total_posts': posts_queryset.count(),
    }

    return render(request, 'blog/posts.html', context)


def post_detail(request, slug):
    post = get_object_or_404(
        Post.objects.select_related('author', 'category').prefetch_related('tags'),
        slug=slug,
        status=Post.Status.PUBLISHED
    )

    post.views_count += 1
    post.save(update_fields=['views_count'])

    related_posts = Post.objects.filter(
        category=post.category,
        status=Post.Status.PUBLISHED
    ).exclude(id=post.id)[:3]

    comments = post.comments.filter(is_approved=True)

    context = {
        'post': post,
        'related_posts': related_posts,
        'comments': comments,
    }
    return render(request, 'blog/post_detail.html', context)


def category_posts(request, category_name):
    """
    Display posts filtered by category

    URL: /category/technology/
    Shows only posts in that category
    """
    posts_queryset = Post.objects.filter(
        status=Post.Status.PUBLISHED
    ).select_related('author', 'category').prefetch_related('tags')

    filtered_posts = posts_queryset.filter(
        category__name__iexact=category_name
    )

    context = {
        'category_name': category_name.title(),
        'posts': filtered_posts,
        'total_posts': len(filtered_posts),
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

    context = {
        'query': query,
        'posts': search_results,
        'total_results': len(search_results),
    }
    return render(request, 'blog/search_results.html', context)


from django.contrib import messages


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
