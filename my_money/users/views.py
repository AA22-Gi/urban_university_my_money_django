from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняет нового пользователя
            return redirect('login')  # Перенаправляет на страницу входа или другую страницу
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('transaction_dashboard')
        else:
            messages.error(request, "Неверные учетные данные.")
    return render(request, 'users/login.html')


def user_exit(request):
    logout(request)
    messages.info(request, "Вы успешно вышли из системы.")
    return redirect('home')  # Перенаправляем на домашнюю страницу или страницу входа