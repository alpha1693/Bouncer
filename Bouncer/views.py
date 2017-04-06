from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import *

def register(request):
    
    if request.method == 'POST':
        context = request.POST.dict()

        if(context["email"] != "" and context["password"] != "" and context["password_confirmation"] != ""):



            return render(request, 'templates/login.html', context)

        else:
            context['error'] = "Must supply email and password"


            return render(request, 'templates/login.html', context)


       
    else :

        return render(request, 'templates/register.html')





    return render(request, 'templates/register.html')



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

        if(context["email"] != "" and context["password"] != ""):

            return render(request, 'templates/login.html', context)

        else:

            context['error'] = "Must supply email and password"

            return render(request, 'templates/login.html', context)


       
    else :
        return render(request, 'templates/login.html')

def changepassword(request):
    if request.method == 'POST':
        


        POST_dict = request.POST.dict()
        email = POST_dict["email"]
        password = POST_dict["password"]

        if(email != "" and password != ""):

            return render(request, 'templates/login.html', {
                'email' :  email,
                'password' :  password

        })

        else:

            return render(request, 'templates/changepassword.html', {
            'error' : "Must supply email and password"
            })



        
    else:
        return render(request, 'templates/changepassword.html')

def hello(request):
    return HttpResponse("Hello world")
