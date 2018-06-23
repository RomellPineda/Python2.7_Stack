from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return 'first_name: ' + self.first_name + ' last_name: ' + self.last_name + ' email: ' + self.email

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 1000)
    uploader = models.ForeignKey(User, related_name = 'my_stuff', null=True)
    liked_by = models.ManyToManyField(User, related_name = 'books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return 'name: ' + self.name + ' description: ' + self.desc