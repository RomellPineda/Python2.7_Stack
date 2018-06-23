from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return 'first_name: ' + self.first_name + ' last_name: ' + self.last_name + ' email: ' + self.email + ' notes: ' + self.notes

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 255)
    by = models.ManyToManyField(Author, related_name = 'books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return 'name: ' + self.name + ' description: ' + self.desc