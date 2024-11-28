from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    """
    Отображает домашнюю страницу приложения.

    Args:
        request (HttpRequest): Объект запроса.

    Returns:
        HttpResponse: Ответ с отрендеренным шаблоном домашней страницы.
    """
    return render(request, 'users/home.html')


def register(request):
    """
    Обрабатывает регистрацию нового пользователя.

    Если запрос является POST-запросом, то форма регистрации обрабатывается.
    В случае успешной валидации пользователя перенаправляют на страницу входа.
    В противном случае отображается форма регистрации.

    Args:
        request (HttpRequest): Объект запроса.

    Returns:
        HttpResponse: Ответ с отрендеренным шаблоном формы регистрации.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняет нового пользователя
            return redirect('login')  # Перенаправляет на страницу входа
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    """
    Обрабатывает вход пользователя в систему.

    Если запрос является POST-запросом, проверяет учетные данные
    пользователя. При успешной аутентификации происходит вход в систему,
    иначе отображается сообщение об ошибке.

    Args:
        request (HttpRequest): Объект запроса.

    Returns:
        HttpResponse: Ответ с отрендеренным шаблоном формы входа.
    """
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
    """
    Выход пользователя из системы.

    Осуществляет выход текущего пользователя и отображает соответствующее
    сообщение. После выхода происходит перенаправление на домашнюю страницу.

    Args:
        request (HttpRequest): Объект запроса.

    Returns:
        HttpResponse: Перенаправляет на домашнюю страницу после выхода.
    """
    logout(request)
    messages.info(request, "Вы успешно вышли из системы.")
    return redirect('home')  # Перенаправляем на домашнюю страницу или страницу входа