from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *
from .services import *

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

        myfile.seek(0)
        parsed_logs = []
        log_file = myfile.read()

        # Create ParsedLog object for each line in log file
        for line in log_file.splitlines():
            tokens = parse_line(line)
            # parse_line returns None if regex fails to match
            if tokens != None:
                parsed_log = ParsedLog(ip_address = tokens[0],rfc_id = tokens[1],user_id = tokens[2],date_time = tokens[3],request_line = tokens[4],http_status = tokens[5],num_bytes = tokens[6])
                parsed_logs.append(parsed_log)
        # Bulk insert into database
        ParsedLog.objects.bulk_create(parsed_logs)


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
