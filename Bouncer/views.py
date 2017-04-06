from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *

def register(request):
    
    if request.method == 'POST':
        context = request.POST.dict()
        form = RegisterForm(request.POST)
        if form.is_valid():
            context['form'] = form
            return render(request, 'templates/register.html', context)
       
    else :

        form = RegisterForm()
        return render(request, 'templates/register.html', {'form': form})



def simple_upload(request):
    context = {}
    if request.method == 'POST' and len(request.FILES) == 0:

        context['error'] = "No file uploaded\n"
         
        return render(request, 'templates/simple_upload.html', context)

    elif request.method == 'POST' and request.FILES['myfile']:
        #needs error checks
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        context['uploaded_file_url'] = uploaded_file_url

        return render(request, 'templates/simple_upload.html', context)

    return render(request, 'templates/simple_upload.html')


def login(request):
    if request.method == 'POST':
        context = request.POST.dict()
        form = LoginForm(request.POST)
        if form.is_valid():
            context['form'] = form
            return render(request, 'templates/login.html', context)
       
    else :
        form = LoginForm()

    return render(request, 'templates/login.html', {'form': form})

def changepassword(request):
    return render(request, 'templates/changepassword.html')

def hello(request):
    return HttpResponse("Hello world")
