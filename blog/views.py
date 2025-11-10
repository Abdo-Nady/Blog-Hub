from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime, date


# Create your views here.


def home(request):
    context = {
        'site_name': 'BlogHub',
        'tagline': 'Your Platform for Sharing Ideas',
        'total_posts': 247,
        'total_authors': 45,
        'current_year': datetime.now().year,
        'featured_topics': [
            'Technology',
            'Design',
            'Travel',
            'Education',
            'Lifestyle'
        ],
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
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'current_year': datetime.now().year,
        'company_name': 'BlogHub Team',
        'founded_year': 2025,
        'mission': 'Empowering writers to share their stories with the world',
        'team_size': 15,
        'values': ['Creativity', 'Community', 'Quality Content', 'Freedom of Expression'],
    }

    return render(request, 'blog/about.html', context)




def posts(request):
    posts_list = [
        {
            'id': 1,
            'title': 'Getting Started with Django',
            'author': 'Sarah Johnson',
            'category': 'Technology',
            'excerpt': 'Learn the fundamentals of Django web development',
            'published': True,
            'date': date(2025, 1, 15),
            'tags': ['Django', 'Python', 'Web Development'],
            'views': 0,
            'reading_time': '5 min'
        },
        {
            'id': 2,
            'title': 'The Psychology of Productivity',
            'author': 'Michael Adams',
            'category': 'Self-Improvement',
            'excerpt': 'How to build strong habits without burning out',
            'published': True,
            'date': date(2025, 2, 1),
            'tags': ['Productivity', 'Habits', 'Self Improvement'],
            'views': 0,
            'reading_time': '6 min'
        },
        {
            'id': 3,
            'title': 'Top 10 UI Mistakes in Modern Web Design',
            'author': 'Emma Clark',
            'category': 'Design',
            'excerpt': 'Avoid these common design pitfalls that reduce user engagement',
            'published': True,
            'date': date(2025, 2, 10),
            'tags': ['UI', 'Design', 'UX'],
            'views': 0,
            'reading_time': '7 min'
        },
        {
            'id': 4,
            'title': 'Exploring Machine Learning with Python',
            'author': 'David Wilson',
            'category': 'Technology',
            'excerpt': 'Why ML matters and how to begin building models',
            'published': False,
            'date': date(2025, 3, 1),
            'tags': ['Python', 'Machine Learning', 'AI'],
            'views': 0,
            'reading_time': '9 min'
        },
        {
            'id': 5,
            'title': 'How to Invest as a Beginner',
            'author': 'Alex Carter',
            'category': 'Business',
            'excerpt': 'Understanding the basics of financial investments',
            'published': True,
            'date': date(2025, 3, 17),
            'tags': ['Business', 'Investment', 'Finance'],
            'views': 0,
            'reading_time': '8 min'
        },
        {
            'id': 6,
            'title': 'Why Reading Every Day Changes You',
            'author': 'Nora Stein',
            'category': 'Lifestyle',
            'excerpt': 'Reading is a superpower that expands thinking',
            'published': True,
            'date': date(2025, 4, 5),
            'tags': ['Lifestyle', 'Reading', 'Habits'],
            'views': 0,
            'reading_time': '6 min'
        },
        {
            'id': 7,
            'title': 'Mastering RESTful APIs',
            'author': 'James Walker',
            'category': 'Technology',
            'excerpt': 'Build scalable and maintainable APIs using best practices',
            'published': True,
            'date': date(2025, 4, 12),
            'tags': ['API', 'REST', 'Backend', 'Web Development'],
            'views': 0,
            'reading_time': '10 min'
        },
        {
            'id': 8,
            'title': 'Healthy Eating for Programmers',
            'author': 'Sophia Baker',
            'category': 'Health',
            'excerpt': 'Tips to stay energized and avoid burnout',
            'published': False,
            'date': date(2025, 5, 1),
            'tags': ['Health', 'Productivity', 'Lifestyle'],
            'views': 0,
            'reading_time': '5 min'
        },
        {
            'id': 9,
            'title': 'The Power of Side Projects',
            'author': 'Chris Morgan',
            'category': 'Career',
            'excerpt': 'How personal projects can transform your professional life',
            'published': True,
            'date': date(2025, 5, 9),
            'tags': ['Career', 'Projects', 'Self Improvement'],
            'views': 0,
            'reading_time': '7 min'
        },
    ]

    context = {
        'page_title': 'All Blog Posts',
        'current_year': datetime.now().year,
        'posts': posts_list,
        'total_posts': len(posts_list),
    }

    return render(request, 'blog/posts.html', context)


def post_detail(request, post_id):
    posts_list = [
        {
            'id': 1,
            'title': 'Getting Started with Django',
            'author': 'Sarah Johnson',
            'category': 'Technology',
            'excerpt': 'Learn the fundamentals of Django web development',
            'published': True,
            'date': date(2025, 1, 15),
            'tags': ['Django', 'Python', 'Web Development'],
            'views': 0,
            'reading_time': '5 min'
        },
        {
            'id': 2,
            'title': 'The Psychology of Productivity',
            'author': 'Michael Adams',
            'category': 'Self-Improvement',
            'excerpt': 'How to build strong habits without burning out',
            'published': True,
            'date': date(2025, 2, 1),
            'tags': ['Productivity', 'Habits', 'Self Improvement'],
            'views': 0,
            'reading_time': '6 min'
        },
        {
            'id': 3,
            'title': 'Top 10 UI Mistakes in Modern Web Design',
            'author': 'Emma Clark',
            'category': 'Design',
            'excerpt': 'Avoid these common design pitfalls that reduce user engagement',
            'published': True,
            'date': date(2025, 2, 10),
            'tags': ['UI', 'Design', 'UX'],
            'views': 0,
            'reading_time': '7 min'
        },
        {
            'id': 4,
            'title': 'Exploring Machine Learning with Python',
            'author': 'David Wilson',
            'category': 'Technology',
            'excerpt': 'Why ML matters and how to begin building models',
            'published': False,
            'date': date(2025, 3, 1),
            'tags': ['Python', 'Machine Learning', 'AI'],
            'views': 0,
            'reading_time': '9 min'
        },
        {
            'id': 5,
            'title': 'How to Invest as a Beginner',
            'author': 'Alex Carter',
            'category': 'Business',
            'excerpt': 'Understanding the basics of financial investments',
            'published': True,
            'date': date(2025, 3, 17),
            'tags': ['Business', 'Investment', 'Finance'],
            'views': 0,
            'reading_time': '8 min'
        },
        {
            'id': 6,
            'title': 'Why Reading Every Day Changes You',
            'author': 'Nora Stein',
            'category': 'Lifestyle',
            'excerpt': 'Reading is a superpower that expands thinking',
            'published': True,
            'date': date(2025, 4, 5),
            'tags': ['Lifestyle', 'Reading', 'Habits'],
            'views': 0,
            'reading_time': '6 min'
        },
        {
            'id': 7,
            'title': 'Mastering RESTful APIs',
            'author': 'James Walker',
            'category': 'Technology',
            'excerpt': 'Build scalable and maintainable APIs using best practices',
            'published': True,
            'date': date(2025, 4, 12),
            'tags': ['API', 'REST', 'Backend', 'Web Development'],
            'views': 0,
            'reading_time': '10 min'
        },
        {
            'id': 8,
            'title': 'Healthy Eating for Programmers',
            'author': 'Sophia Baker',
            'category': 'Health',
            'excerpt': 'Tips to stay energized and avoid burnout',
            'published': False,
            'date': date(2025, 5, 1),
            'tags': ['Health', 'Productivity', 'Lifestyle'],
            'views': 0,
            'reading_time': '5 min'
        },
        {
            'id': 9,
            'title': 'The Power of Side Projects',
            'author': 'Chris Morgan',
            'category': 'Career',
            'excerpt': 'How personal projects can transform your professional life',
            'published': True,
            'date': date(2025, 5, 9),
            'tags': ['Career', 'Projects', 'Self Improvement'],
            'views': 0,
            'reading_time': '7 min'
        },
    ]

    post = next((p for p in posts_list if p['id'] == post_id), None)

    if post is None:
        raise Http404(f"Post {post_id} not found")

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)


def category_posts(request, category_name):
    """
    Display posts filtered by category

    URL: /category/technology/
    Shows only posts in that category
    """

    posts_list = [
        {
            'id': 1,
            'title': 'Getting Started with Django',
            'author': 'Sarah Johnson',
            'category': 'Technology',
            'excerpt': 'Learn the fundamentals of Django web development',
            'published': True,
            'date': date(2025, 1, 15),
            'tags': ['Django', 'Python', 'Web Development'],
            'views': 0,
            'reading_time': '5 min'
        },
        {
            'id': 2,
            'title': 'The Psychology of Productivity',
            'author': 'Michael Adams',
            'category': 'Self-Improvement',
            'excerpt': 'How to build strong habits without burning out',
            'published': True,
            'date': date(2025, 2, 1),
            'tags': ['Productivity', 'Habits', 'Self Improvement'],
            'views': 0,
            'reading_time': '6 min'
        },
        {
            'id': 3,
            'title': 'Top 10 UI Mistakes in Modern Web Design',
            'author': 'Emma Clark',
            'category': 'Design',
            'excerpt': 'Avoid these common design pitfalls that reduce user engagement',
            'published': True,
            'date': date(2025, 2, 10),
            'tags': ['UI', 'Design', 'UX'],
            'views': 0,
            'reading_time': '7 min'
        },
        {
            'id': 4,
            'title': 'Exploring Machine Learning with Python',
            'author': 'David Wilson',
            'category': 'Technology',
            'excerpt': 'Why ML matters and how to begin building models',
            'published': False,
            'date': date(2025, 3, 1),
            'tags': ['Python', 'Machine Learning', 'AI'],
            'views': 0,
            'reading_time': '9 min'
        },
        {
            'id': 5,
            'title': 'How to Invest as a Beginner',
            'author': 'Alex Carter',
            'category': 'Business',
            'excerpt': 'Understanding the basics of financial investments',
            'published': True,
            'date': date(2025, 3, 17),
            'tags': ['Business', 'Investment', 'Finance'],
            'views': 0,
            'reading_time': '8 min'
        },
        {
            'id': 6,
            'title': 'Why Reading Every Day Changes You',
            'author': 'Nora Stein',
            'category': 'Lifestyle',
            'excerpt': 'Reading is a superpower that expands thinking',
            'published': True,
            'date': date(2025, 4, 5),
            'tags': ['Lifestyle', 'Reading', 'Habits'],
            'views': 0,
            'reading_time': '6 min'
        },
        {
            'id': 7,
            'title': 'Mastering RESTful APIs',
            'author': 'James Walker',
            'category': 'Technology',
            'excerpt': 'Build scalable and maintainable APIs using best practices',
            'published': True,
            'date': date(2025, 4, 12),
            'tags': ['API', 'REST', 'Backend', 'Web Development'],
            'views': 0,
            'reading_time': '10 min'
        },
        {
            'id': 8,
            'title': 'Healthy Eating for Programmers',
            'author': 'Sophia Baker',
            'category': 'Health',
            'excerpt': 'Tips to stay energized and avoid burnout',
            'published': False,
            'date': date(2025, 5, 1),
            'tags': ['Health', 'Productivity', 'Lifestyle'],
            'views': 0,
            'reading_time': '5 min'
        },
        {
            'id': 9,
            'title': 'The Power of Side Projects',
            'author': 'Chris Morgan',
            'category': 'Career',
            'excerpt': 'How personal projects can transform your professional life',
            'published': True,
            'date': date(2025, 5, 9),
            'tags': ['Career', 'Projects', 'Self Improvement'],
            'views': 0,
            'reading_time': '7 min'
        },
    ]

    if category_name != category_name.lower():
        return redirect('blog:category_posts', category_name=category_name.lower())

    filtered_posts = [
        post for post in posts_list
        if post['category'].lower() == category_name
    ]

    context = {
        'category_name': category_name.title(),
        'posts': filtered_posts,
        'total_posts': len(filtered_posts),
    }
    return render(request, 'blog/category_posts.html', context)


def search_posts(request):
    """
    Search posts by title or content

    URL: /search/?q=django

    """
    # Get a search query from URL parameters
    query = request.GET.get('q', '')  # Default to empty string if no query

    # All posts
    posts_list = [
        {
            'id': 1,
            'title': 'Getting Started with Django',
            'author': 'Sarah Johnson',
            'category': 'Technology',
            'excerpt': 'Learn the fundamentals of Django web development',
            'published': True,
            'date': date(2025, 1, 15),
            'tags': ['Django', 'Python', 'Web Development'],
            'views': 0,
            'reading_time': '5 min'
        },
        {
            'id': 2,
            'title': 'The Psychology of Productivity',
            'author': 'Michael Adams',
            'category': 'Self-Improvement',
            'excerpt': 'How to build strong habits without burning out',
            'published': True,
            'date': date(2025, 2, 1),
            'tags': ['Productivity', 'Habits', 'Self Improvement'],
            'views': 0,
            'reading_time': '6 min'
        },
        {
            'id': 3,
            'title': 'Top 10 UI Mistakes in Modern Web Design',
            'author': 'Emma Clark',
            'category': 'Design',
            'excerpt': 'Avoid these common design pitfalls that reduce user engagement',
            'published': True,
            'date': date(2025, 2, 10),
            'tags': ['UI', 'Design', 'UX'],
            'views': 0,
            'reading_time': '7 min'
        },
        {
            'id': 4,
            'title': 'Exploring Machine Learning with Python',
            'author': 'David Wilson',
            'category': 'Technology',
            'excerpt': 'Why ML matters and how to begin building models',
            'published': False,
            'date': date(2025, 3, 1),
            'tags': ['Python', 'Machine Learning', 'AI'],
            'views': 0,
            'reading_time': '9 min'
        },
        {
            'id': 5,
            'title': 'How to Invest as a Beginner',
            'author': 'Alex Carter',
            'category': 'Business',
            'excerpt': 'Understanding the basics of financial investments',
            'published': True,
            'date': date(2025, 3, 17),
            'tags': ['Business', 'Investment', 'Finance'],
            'views': 0,
            'reading_time': '8 min'
        },
        {
            'id': 6,
            'title': 'Why Reading Every Day Changes You',
            'author': 'Nora Stein',
            'category': 'Lifestyle',
            'excerpt': 'Reading is a superpower that expands thinking',
            'published': True,
            'date': date(2025, 4, 5),
            'tags': ['Lifestyle', 'Reading', 'Habits'],
            'views': 0,
            'reading_time': '6 min'
        },
        {
            'id': 7,
            'title': 'Mastering RESTful APIs',
            'author': 'James Walker',
            'category': 'Technology',
            'excerpt': 'Build scalable and maintainable APIs using best practices',
            'published': True,
            'date': date(2025, 4, 12),
            'tags': ['API', 'REST', 'Backend', 'Web Development'],
            'views': 0,
            'reading_time': '10 min'
        },
        {
            'id': 8,
            'title': 'Healthy Eating for Programmers',
            'author': 'Sophia Baker',
            'category': 'Health',
            'excerpt': 'Tips to stay energized and avoid burnout',
            'published': False,
            'date': date(2025, 5, 1),
            'tags': ['Health', 'Productivity', 'Lifestyle'],
            'views': 0,
            'reading_time': '5 min'
        },
        {
            'id': 9,
            'title': 'The Power of Side Projects',
            'author': 'Chris Morgan',
            'category': 'Career',
            'excerpt': 'How personal projects can transform your professional life',
            'published': True,
            'date': date(2025, 5, 9),
            'tags': ['Career', 'Projects', 'Self Improvement'],
            'views': 0,
            'reading_time': '7 min'
        },
    ]

    if not query:
        search_results = posts_list
    else:
        search_results = [
            post for post in posts_list
            if query.lower() in post['title'].lower() or
               query.lower() in post['excerpt'].lower()
        ]

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
        'phone': '+1-800-BLOGHUB',
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

