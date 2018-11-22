from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# import bcrypt
# import re
# import stripe

# Create your views here.
def index(request):
    return render(request, 'food_app/index.html')