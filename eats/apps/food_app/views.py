from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from .models import *
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    return render(request, 'food_app/index.html')

def menu(request):
    return render(request, 'food_app/menu.html')

def auth(request):
    return render(request, 'food_app/reg.html')

def validate(request):
    return render(request, 'food_app/login.html')

def register(request):
    if request.method != 'POST':
        return redirect('/register')
    error = False
    if len(request.POST['first_name']) < 2:
        messages.error(request,'Name must be 2 or more characters')
        error = True
    if not request.POST['first_name'].isalpha() or not request.POST['last_name'].isalpha():
        messages.error(request,'First and last name must not contain numbers or spaces')
        error = True
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request,'Invalid email')
        error = True
    if len(User.objects.filter(email = request.POST['email'])) > 0:
        messages.error(request,'User already exsist')
        error = True
    if len(request.POST['password']) < 8:
        messages.error(request,'Password must be 8 or more characters in length')
        error = True
    if request.POST['password'] != request.POST['confirm_pw']:
        messages.error(request,'Password and confirm password must match')
        error = True
    if len(request.POST['address']) < 1:
        messages.error(request,'Address cannot be blank')
        error = True
    if len(request.POST['city']) < 1:
        messages.error(request,'Please provide city')
        error = True
    if len(request.POST['state']) < 1:
        messages.error(request,'Please provide state')
        error = True
    if not request.POST['zip_code'].isnumeric():
        messages.error(request, 'Zip code gotta be all numbers Sugar!')
        error = True
    if error:
        return redirect('/register')
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashed)
        request.session['user_id'] = user.id
        request.session['user_name'] = user.first_name
        print(user.id)
        print(user.first_name)
    return redirect('/home')

def login(request):
    if request.method != 'POST':
        return redirect('/login')
    user = User.objects.filter(email = request.POST['email'])
    if len(user) > 0:
        shmuser = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), shmuser.password.encode()):
            request.session['user_id'] = shmuser.id
            request.session['user_name'] = shmuser.first_name
            return redirect('/home')
        else:
            messages.error(request, 'Email or password invalid' )
            return redirect('/login')
    else:
        messages.error(request, 'Email or password invalid')
        return redirect('/login')

def home(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        'user' : User.objects.get(id = request.session['user_id']),
        # 'myjobs' : Job.objects.filter(Q(posted_by_id=request.session['user_id'])|Q(worker=request.session['user_id'])).order_by('created_at'),
        # 'otherjobs' : Job.objects.exclude(posted_by_id=request.session['user_id']).exclude(worker__id=request.session['user_id']).order_by('created_at'),
    }
    return render(request, 'handy_app/home.html', context)
