from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Account

class RegiserUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('image',)