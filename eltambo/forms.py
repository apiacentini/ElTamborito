from django import forms
from django.forms import widgets
from django.core.validators import validate_email
from .models import Utente
from django.contrib.auth import authenticate, login, logout


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=3, required=True)
    nome = forms.CharField(min_length=3, max_length=30, required=True)
    cognome = forms.CharField(min_length=3, max_length=30, required=True)
    email = forms.CharField(min_length=3, max_length=50, required=True, validators=[validate_email])
    password = forms.CharField(widget=widgets.PasswordInput(), required=True, min_length=5, max_length=32)


