from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout


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
    form = RegisterForm(request.POST or None)  # Создаем форму, даже если это GET-запрос

    if request.method == 'POST' and form.is_valid():  # Проверяем, валидна ли форма
        form.save()  # Сохраняет нового пользователя
        return redirect('login')  # Перенаправляет на страницу входа

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
    form = LoginForm(request, data=request.POST or None)  # Создаем форму, даже если это GET-запрос

    if request.method == 'POST' and form.is_valid():  # Проверяем, валидна ли форма
        user = form.get_user()  # Получаем пользователя из формы
        login(request, user)  # Входим в систему
        return redirect('transaction_dashboard')  # Перенаправление на дашборд

    return render(request, 'users/login.html', {'form': form})


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
    return redirect('home')  # Перенаправляем на домашнюю страницу или страницу входа
