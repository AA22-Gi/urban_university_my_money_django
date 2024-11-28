from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser ):
    """
    Пользовательская модель для учета дополнительной информации о пользователе.

    Эта модель расширяет стандартную модель пользователя Django, добавляя
    поля для возраста и пола. Также переопределяются поля 'first_name'
    и 'last_name', чтобы они не использовались в данной модели.

    Атрибуты:
        age (PositiveIntegerField): Возраст пользователя. Может быть null или пустым.
        gender (CharField): Пол пользователя. Может принимать значения 'M' (мужской) или 'F' (женский).

    Примечание:
        Переопределенные поля 'first_name' и 'last_name' убраны из модели, чтобы избежать их использования.
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
