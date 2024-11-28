from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    """
    Форма регистрации нового пользователя.

    Эта форма расширяет стандартную форму UserCreationForm и позволяет
    пользователю вводить дополнительную информацию, такую как возраст и пол,
    помимо стандартных полей.

    Атрибуты:
        Meta: Класс, который определяет модель, которую будет использовать форма,
              и список полей для ввода.
              Поля:
                  - model (User): Модель пользователя, к которой относится форма.
                  - fields (list): Список полей, которые будут включены в форму.
                  - labels (dict): Словарь меток для полей формы.
    """

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