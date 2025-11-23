from django.contrib import admin
from django.urls import path
from . import views

from .views import MyPostsView, DraftPostsView, LoginView, RegisterView, UserLogoutView

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),

    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),

    path('logout/', UserLogoutView.as_view(), name='logout'),

    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("posts/", views.posts, name="posts"),
    path('my-posts/', MyPostsView.as_view(), name='my_posts'),

    path('post/<str:slug>/update', views.post_update, name='post-update'),
    path("post/<str:slug>/delete", views.post_delete, name="post_delete"),
    path('drafts/', DraftPostsView.as_view(), name='draft_posts'),
    path('post/create/', views.post_create, name='post-create'),
    path("post/<str:slug>/", views.post_detail, name="post_detail"),

    path("category/<str:category_name>/", views.category_posts, name="category_posts"),
    path("search/", views.search_posts, name="search_posts"),
    path("author/<str:author_name>/", views.author_posts, name="author_posts"),
    path("post/<slug:slug>/comment/", views.add_comment, name='add_comment'),
    path("comment/<int:comment_id>/delete/", views.delete_comment, name='delete_comment'),
]
