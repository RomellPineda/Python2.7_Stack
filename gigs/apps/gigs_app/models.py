from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate_register(self, postData):
    error = False
    if len(postData['first_name']) < 2:
        messages.error(request,'Name must be 2 or more characters')
        error = True
    if not postData['first_name'].isalpha() or not postData['last_name'].isalpha():
        messages.error(request,'First and last name must not contain numbers or spaces')
        error = True
    if not EMAIL_REGEX.match(postData['email']):
        messages.error(request,'Invalid email')
        error = True
    if len(User.objects.filter(email = postData['email'])) > 0:
        messages.error(request,'User already exsist')
        error = True
    if len(postData['password']) < 8:
        messages.error(request,'Password must be 8 or more characters in length')
        error = True
    if postData['password'] != postData['confirm_pw']:
        messages.error(request,'Password and confirm password must match')
        error = True

class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Job(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField()
    location = models.CharField(max_length = 100)

    posted_by = models.ForeignKey(User, related_name = 'jobs', null=True)
    worker = models.ManyToManyField(User, related_name = 'working')
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)