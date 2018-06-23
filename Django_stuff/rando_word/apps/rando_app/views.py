from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return render(request, 'rando_app/index.html')

def rando_word(request):
    request.session['wurd'] = get_random_string(length=14)
    print('gen triggered' * 19)
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 0
    return redirect('/result')

def result(request):
    print('result triggered' * 19)
    return render(request, 'rando_app/index.html')