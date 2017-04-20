import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import *

from django.utils import timezone
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core import mail

# view for homepage - index
class MainView(generic.ListView):
    template_name = 'account/main.html'
    context_object_name = 'log_list'

    def get_queryset(self):
        return ParsedLog.objects.all().order_by('-pub_date')
