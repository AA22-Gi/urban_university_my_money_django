from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'age', 'gender', 'email', 'password1', 'password2']
        labels = {
            'age': 'Возраст',
            'gender': 'Пол',
            'email': 'Электронная почта',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
        }