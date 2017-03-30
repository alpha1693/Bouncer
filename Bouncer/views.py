from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import *

def simple_upload(request):

    if request.method == 'POST' and len(request.FILES) == 0:
        error = "No file uploaded\n"
         
        return render(request, 'templates/simple_upload.html', {
            'error' : error
        })


    elif request.method == 'POST' and request.FILES['myfile']:
        #needs error checks
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
        log_file = myfile.chunks()
        parsed_logs = []
        for line in log_file:
            tokens = ParsedLog.parse_line(line)
            if tokens == None:
                continue
            else:
                parsed_logs.append(ParsedLog(tokens))

        ParsedLog.objects.bulk_create(parsed_logs)

        return render(request, 'templates/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'error' : error
        })
    return render(request, 'templates/simple_upload.html')


def login(request):
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

            return render(request, 'templates/login.html', {
            'error' : "Must supply email and password"
            })


       
    else :
        return render(request, 'templates/login.html')


def hello(request):
    return HttpResponse("Hello world")
