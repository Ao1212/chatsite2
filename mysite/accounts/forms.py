from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class SingUpForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True, help_text="ユーザーネーム", label="username")
    email = forms.EmailField(max_length=200, help_text="メールアドレス", label="email")
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileForm(forms.Form):
    username = forms.CharField(max_length=20, label="ユーザーネーム")
    email = forms.EmailField(max_length=200, label="メールアドレス")
