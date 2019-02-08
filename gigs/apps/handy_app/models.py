from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Job(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField()
    location = models.CharField(max_length = 100)

    posted_by = models.ForeignKey(User, related_name = 'jobs', null=True)
    worker = models.ManyToManyField(User, related_name = 'working')
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)