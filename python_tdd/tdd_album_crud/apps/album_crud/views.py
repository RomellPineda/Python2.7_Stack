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

def update(request, id):
    album = Album.objects.get(id = id)
    album.title = request.POST['title']
    album.artist = request.POST['artist']
    album.year = request.POST['year']
    album.save()
    context = {
        'album' : Album.objects.get(id = id)
    }
    return redirect('/', context)

def delete(request, id):
    da = Album.objects.get(id = id)
    da.delete()
    return redirect('/')