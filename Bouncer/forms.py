from django import forms
from .models import *


class LoginForm(forms.Form):

	email = forms.EmailField(
		max_length = 20,
        label="Email",
    )

	password = forms.CharField(
		max_length = 20,
		label = "Password",
		widget = forms.PasswordInput(),
    )


class RegisterForm(forms.Form):

	email = forms.EmailField(
		max_length = 20,
        label="Email",
    )

	password = forms.CharField(
		max_length = 20,
		label = "Password",
		widget = forms.PasswordInput(),
    )

	password_confirmation = forms.CharField(
		max_length = 20,
		label = "Confirm Password",
		widget = forms.PasswordInput(),
    )
