from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print('// Go flight ' * 20)
    return render(request, 'sesh_app/index.html')

def sent(request):
    print(' // splash over' * 10)
    return redirect('/processed')

def result():
    print(' // splash out' * 10)
    return render(request, 'sesh_app/index.html')