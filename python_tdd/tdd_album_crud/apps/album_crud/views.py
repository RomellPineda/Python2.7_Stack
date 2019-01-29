from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, "index.html")

def add(request):
    return redirect('/')

def edit(request):
    return redirect('/')

def delete(request):
    return redirect('/')