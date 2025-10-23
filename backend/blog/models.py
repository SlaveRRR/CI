# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_authors'

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_categories'
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_posts'
        ordering = ['-created_at']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.title}"

    class Meta:
        db_table = 'blog_comments'
        ordering = ['-created_at']