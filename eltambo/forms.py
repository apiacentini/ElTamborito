from django import forms
from django.forms import widgets
from django.core.validators import validate_email


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(min_length=3, max_length=30, required=True)
    last_name = forms.CharField(min_length=3, max_length=30, required=True)
    email = forms.CharField(min_length=3, max_length=50, required=True, validators=[validate_email])
    password = forms.CharField(widget=widgets.PasswordInput(), required=True, min_length=5, max_length=32)
    nazione = forms.CharField(min_length=3, max_length=30, required=True)
    citta = forms.CharField(min_length=3, max_length=30, required=True)
    via = forms.CharField(min_length=3, max_length=30, required=True)
    provincia = forms.CharField(min_length=3, max_length=30, required=True)
    cap = forms.CharField(min_length=5, max_length=5, required=True)