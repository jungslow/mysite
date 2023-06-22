from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):       # 회원가입에 사용될 UserForm
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")
