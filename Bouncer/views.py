from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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
        

        return render(request, 'templates/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'error' : error
        })
    return render(request, 'templates/simple_upload.html')

def home(request):
    return render(request, 'templates/base.html')

def hello(request):
    return HttpResponse("Hello world")
