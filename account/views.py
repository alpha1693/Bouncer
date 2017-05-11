import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import *
from .services import *

from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import mail

# view for homepage - index


class MainView(generic.ListView):
    template_name = 'account/main.html'
    context_object_name = 'log_list'

    def post(self, request, *args, **kwargs):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        myfile.seek(0)
        parsed_logs = []
        log_file = myfile.read()

        # Create ParsedLog object for each line in log file
        for line in log_file.splitlines():
            tokens = parse_line(line)
            # parse_line returns None if regex fails to match
            if tokens != None:
                parsed_log = ParsedLog(owner=request.user, ip_address=tokens[0], rfc_id=tokens[1], user_id=tokens[
                                       2], date_time=tokens[3], request_line=tokens[4], http_status=tokens[5], num_bytes=tokens[6])
                parsed_logs.append(parsed_log)
        # Bulk insert into database
        ParsedLog.objects.bulk_create(parsed_logs)
        return render(request, 'account/main.html', {'error': "Upload Successful"})

    def get_queryset(self):
        return ParsedLog.objects.all().order_by('-pub_date')
