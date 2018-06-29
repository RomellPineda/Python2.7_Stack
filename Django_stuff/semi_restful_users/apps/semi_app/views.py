from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
    context = {
        'users' : User.objects.all()
    }
    return render(request, 'semi_app/index.html', context)

def new(request):
    return render(request, 'semi_app/new.html')

def create(request):
    if request.method != 'POST':
        return redirect('/users')
    error = False
    if len(request.POST['first_name']) < 2:
        print('First name must be 2 or more characters')
        error = True
    if len(request.POST['last_name']) < 2:
        print('Last name must be 2 or more characters')
        error = True
    if not request.POST['first_name'].isalpha() or not request.POST['last_name'].isalpha():
        print('First and Last name must not contain numbers')
        error = True
    # if not EMAIL_REGEX.match(request.POST['email']): !!!not operational
    #     print('Email is invalid')
    #     error = True
    if error:
        print('One or more errors triggered')
        return redirect('/users')
    else:
        print('its on my dude!')
        # hashed = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        # request.session['user_id'] = user.id !!!if user = User.objects.create...
        return redirect('/users')

def show(request, number):
    print(' // all show ' * 20)
    cont = {'user' : User.objects.get(id = number)}
    return render(request, 'semi_app/show.html', cont)

def edit(request, number):
    print(' // in edit ' *10)
    cont = {'user' : User.objects.get(id = number)}

    return render(request, 'semi_app/edit.html', cont)

def update(request, number):
    if request.method != 'POST':
        return redirect('/users')
    error = False
    if len(request.POST['first_name']) < 2:
        print('First name must be 2 or more characters')
        error = True
    if len(request.POST['last_name']) < 2:
        print('Last name must be 2 or more characters')
        error = True
    if not request.POST['first_name'].isalpha() or not request.POST['last_name'].isalpha():
        print('First and Last name must not contain numbers')
        error = True
    # if not EMAIL_REGEX.match(request.POST['email']): !!!not operational
    #     print('Email is invalid')
    #     error = True
    if error:
        print('One or more errors triggered')
        return redirect('/users')
    else:
        print('// 2nd validation cleared procesed update' * 10)
        change = User.objects.get(id=number)
        change.first_name = request.POST['first_name']
        change.last_name = request.POST['last_name']
        change.email = request.POST['email']
        change.save()
        # hashed = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
        # request.session['user_id'] = user.id !!!if user = User.objects.create...
        return redirect('/users')

def delete(request, number):
    delete = User.objects.get(id=number)
    delete.delete()
    return redirect('/users')