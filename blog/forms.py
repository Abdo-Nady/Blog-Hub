# blog/forms.py
from django import forms
from .models import Post, Category, Tag


class PostForm(forms.ModelForm):
    new_category = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_tags = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Comma separated tags'}))

    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'category', 'tags', 'status', 'is_featured', 'allow_comments']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Short summary'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Write your post content'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'allow_comments': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
