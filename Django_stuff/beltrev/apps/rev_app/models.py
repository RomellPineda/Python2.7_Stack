from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100)
    alias = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    review = models.TextField()
    rating = models.IntegerField()
    uploader = models.ForeignKey(User, related_name = 'books', null = True)
    reviewer = models.ManyToManyField(User, related_name = 'rev_books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)