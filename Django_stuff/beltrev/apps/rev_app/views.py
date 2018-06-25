from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
    return render(request, 'rev_app/index.html')

def register(request):
    print('register process triggered ' * 10)
    if request.method != 'POST':
        return redirect('/')
    error = False
    if len(request.POST['name']) < 2:
        print('Name must be 2 or more characters')
        error = True
    # if not request.POST['name'].isalpha():
    #     print('Name must not contain numbers')
    #     error = True
    if not EMAIL_REGEX.match(request.POST['email']):
        print('Invalid email')
        error = True
    if len(User.objects.filter(email = request.POST['email'])) > 0:
        print('User already exsist')
        error = True
    if len(request.POST['password']) < 8:
        print('Password must be 8 or more characters in length')
        error = True
    if request.POST['password'] != request.POST['confirm_pw']:
        print('Password and confirm password must match')
        error = True
    if error:
        return redirect('/')
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        print(hashed)
        user = User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], password = hashed)
        request.session['user_id'] = user.id
        request.session['user_name'] = user.name
    return redirect('/home')

def login(request):
    print('login process triggered')
    if request.method != 'POST':
        return redirect('/')
    user = User.objects.filter(email = request.POST['email'])[0]

    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        print('Password match')
        request.session['user_id'] = user.id
        request.session['user_name'] = user.name
        return redirect('/home')
    else:
        print('Password failed ' * 10)
        return redirect('/')

def home(request):
    wusgood = {
        'latest' : Book.objects.order_by('updated_at')[:3],
        'other' : Book.objects.order_by('updated_at')[3:],
    }
    print('home triggered')
    return render(request, 'rev_app/home.html', wusgood)

def add(request):
    return render(request, 'rev_app/add.html')

def newbook(request):
    if request.method != 'POST':
        return redirect('/')
    print(request.POST)
    return redirect('/book_info')

def info(request):
    return render(request, 'rev_app/book_info.html')

def review(request):
    return render(request, 'rev_app/review.html')

def logout(request):
    request.session.clear()
    return redirect('/')