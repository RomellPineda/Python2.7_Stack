from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print('/// currently in server ' * 10)
    response = "Placeholder blogs Cupcake ipsum dolor. Sit amet croissant cotton candy. Oat cake candy canes dessert bear claw lemon drops."
    return HttpResponse(response)

def newblog(request):
    response = "New placeholder to display a new form to create a new blog!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    return HttpResponse(response)

def create(request):
    print('created method triggered' * 20)
    return redirect('/')

def num(request, number):
    print('/// number ' * 20)
    response = "Place holder " + number
    return HttpResponse(response, number)

def numedit(request, number):
    response = "Place holder " + number
    return HttpResponse(response, number)

def dele(request, number):
    return redirect('/')