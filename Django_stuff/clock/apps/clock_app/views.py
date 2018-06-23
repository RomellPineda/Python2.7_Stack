from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = { 'time' : strftime('%Y-%m-%D %H: %M: %S', gmtime())}
    return render(request, 'clock_app/index.html', context)