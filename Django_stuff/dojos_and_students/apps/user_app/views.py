from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Hello, I am django preflight for users!"
    return HttpResponse(response)
