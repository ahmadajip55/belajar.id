from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms

from belajar.apps.users.models import User


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password'].widget.attrs['placeholder'] = 'password'


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['full_name'].widget.attrs['placeholder'] = 'fullname'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['phone'].widget.attrs['placeholder'] = 'phone'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'