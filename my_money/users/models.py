from django.db import models


class User(models.Model):
    """
        Модель для представления пользователя.

        Атрибуты:
            name (str): Имя пользователя.
            surname (str): Фамилия пользователя.
            age (int, optional): Возраст пользователя, может быть пустым.
            gender (str): Пол пользователя ('M' для мужского, 'F' для женского).
            email (str): Электронная почта пользователя, должна быть уникальной.
            password (str): Пароль пользователя.
        """

    GENDER_CHOICES = [
        ('M', 'мужской'),
        ('F', 'женский'),
    ]

    name = models.CharField(max_length=20)  # Имя
    surname = models.CharField(max_length=20)  # Фамилия
    age = models.PositiveIntegerField(null=True)  # Возраст
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)  # Пол
    email = models.EmailField(unique=True)  # Почта
    password = models.CharField(max_length=128)  # Пароль

    def __str__(self):
        return f"{self.name} {self.surname}"
