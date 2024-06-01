# accounts/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
