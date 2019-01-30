from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        Album.objects.create(title = request.POST['title'], artist = request.POST['artist'], year = request.POST['year'])
    return redirect('/')

def read(request):
    context = {
        'albums' : Album.objects.all()
    }
    return render(request, 'index.html', context)

def update(request):
    return redirect('/')

def delete(request):
    da = Album.objects.get(id = 1)
    da.delete()
    return redirect('/')