from django.shortcuts import render, redirect
from .forms import LoginForm


def home(request):
    return render(request, 'users_html/home.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Обработка данных, аутентификация пользователя и т.п.
            return redirect('transaction_dashboard')  # Перенаправление на домашнюю страницу
    else:
        form = LoginForm()

    return render(request, 'users_html/login.html', {'form': form})
