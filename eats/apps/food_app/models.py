from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class User(models.Model):
    # admin = models.BooleanField(default=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_two = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' | ' + self.last_name + ' | ' + self.email

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.TextField()
    purchaser = models.ManyToManyField(User, related_name = 'products')
    price = models.ForeignKey(Price, related_name ='product_price')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name = 'ingredients')

class Price(models.Model):
    price = models.IntegerField()