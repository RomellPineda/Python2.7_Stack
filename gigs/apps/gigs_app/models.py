from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate_register(self, postData):
    error = {}
    if len(postData['first_name']) < 2:
        error['first'] = 'Name must be 2 or more characters'
    if not postData['first_name'].isalpha() or not postData['last_name'].isalpha():
        error.['num'] = 'First and last name must not contain numbers or spaces'
    if not EMAIL_REGEX.match(postData['email']):
        error.['email'] = 'Invalid email'
    if len(User.objects.filter(email = postData['email'])) > 0:
        error.['already'] = 'User already exsist'
    if len(postData['password']) < 8:
        error.['password'] = 'Password must be 8 or more characters in length'
    if postData['password'] != postData['confirm_pw']:
        error.['passcon'] = 'Password and confirm password must match'
    # return error
    if len(error):
        return error
    result = {}
    hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = hashed)
    result['success'] = user
    return result

    def login(self, postData):
        a_user = User.objects.filter(email =  postData['email'])
        if len(a_user) > 0:
            user = a_user[0]
            if bcrypt.checkpw(postData['passoword'].encode(), user.password.encode()):
                return {'success' : user}
            else:
                return {}
        else:
            return {}

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