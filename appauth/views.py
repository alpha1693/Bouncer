import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import *

from django.utils import timezone
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def forgot_password(request):
    # If it's a HTTP POST, we'll process the form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        form = forgotPasswordForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        if form.is_valid():
            print('form is good')
            user = User.objects.filter(username = username, email = email)
            if user:
                return HttpResponse("Please check your email to reset your password.")
            
            else:
                return render(request, 'forgotpassword.html', {'error' : 'Username and/or Email were not found. Please try again.'})
            
        else:
            return render(request, 'forgotpassword.html', {'error' : 'Credentials not valid. Please try again.'})
    else:
        return render(request, 'forgotpassword.html', {})

def register(request):
    
    registered = False
    
    # If it's a HTTP POST, we'll process the form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.

        user_form = UserForm(data=request.POST)
        # If the form is valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            
            # Hash the password with the set_password method
            user.set_password(user.password)
            user.save()
            # Update our variable to tell the template registration was successful.
            registered = True
            return HttpResponse("Please check your email for a verification link for your account.")


        else:
            return render(request, 'register.html', {'error': 'Registration credentials are not valid. Please try again.' , 'user_form': user_form, 'registered': registered})

# Not a HTTP POST, so we render our form using our ModelForm instance.
# These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
    return render(request, 'register.html', {'user_form': user_form, 'registered': registered})
 

def user_login(request):
    # If it's a HTTP POST, we'll process the form data.
    if request.method == 'POST':
        #grab information from the raw form information.
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the username/password combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('account:main'))
            return HttpResponse("Your account is disabled.")
        else:
            return render(request, 'login.html', {'error': 'Invalid login details. Please try again.'})

	
# Display the login form.
    else:
        return render(request, 'login.html', {})


@login_required #Django enforced authentication control
def displaySettings(request):
    
    return render(request, 'settings.html', {})

@login_required #Django enforced authentication control
def changePasswordView(request):
    return render(request, 'changepassword.html', {})

@login_required #Django enforced authentication control
def updateSettings(request):
    # If it's a HTTP POST, we'll process the form data.
    if request.method == 'POST':
          #grab information from the raw form information.
        updatedEmail = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if first_name == "" or last_name == "":
            return HttpResponse("Please enter both a first and last name")
	
    try:
        validate_email(updatedEmail)
    except ValidationError as e:
        return HttpResponse("Invalid email")
    else:
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = updatedEmail
        request.user.save()
	
    return HttpResponseRedirect(reverse('appauth:settings'))    

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('account:main'))
    
@login_required
def changepassword(request):
    user = request.user
    old = request.POST['oldpassword']
    new = request.POST['newpassword']
    if user.check_password(old):
        user.set_password(new)
        user.save()
        return HttpResponseRedirect(reverse('account:main'))
    else:
        return HttpResponse("The password you entered is wrong.")