from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegisterForm(UserCreationForm):
    """
    Форма регистрации нового пользователя.

    Эта форма расширяет стандартную форму UserCreationForm из Django и позволяет
    пользователю вводить дополнительную информацию, такую как возраст и пол,
    помимо стандартных полей для регистрации.

    Атрибуты:
        Meta: Класс определяющий модель, которую будет использовать форма, и список полей для ввода.
            Поля:
                model (User): Модель пользователя, к которой относится форма.
                fields (list): Список полей, которые будут включены в форму.
                    - 'username': Уникальное имя пользователя (обязательное поле).
                    - 'age': Возраст пользователя (необязательное поле).
                    - 'gender': Пол пользователя (необязательное поле).
                    - 'email': Электронная почта пользователя (необязательное поле).
                    - 'password1': Пароль для аккаунта (обязательное поле).
                    - 'password2': Подтверждение пароля (обязательное поле).
                labels (dict): Словарь меток для полей формы.
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


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
        }