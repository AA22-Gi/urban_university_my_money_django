from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Модель для учета информации о пользователе.

    Эта модель расширяет стандартную модель пользователя Django, добавляя поля для возраста и пола.
    Поля 'first_name' и 'last_name' переопределены,
    чтобы их использование было исключено из данной модели, так как они не требуются.

    Атрибуты:
        age (PositiveIntegerField): Возраст пользователя. Может быть null или пустым.
        gender (CharField): Пол пользователя. Может принимать значения 'M' (мужской) или 'F' (женский).
    """
    GENDER_CHOICES = [
        ('M', 'мужской'),
        ('F', 'женский')
    ]

    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)

    # Переопределяем поля first_name и last_name, чтобы они не использовались
    first_name = None
    last_name = None
