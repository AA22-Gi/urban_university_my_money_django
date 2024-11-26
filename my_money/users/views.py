from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm


def home(request):
    return render(request, 'users/home.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # Обработка данных, аутентификация пользователя и т.п.
            return redirect('transaction_dashboard')  # Перенаправление на домашнюю страницу
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу авторизации после регистрации
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})