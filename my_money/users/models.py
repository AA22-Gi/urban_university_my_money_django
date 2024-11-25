from django.db import models


class User(models.Model):
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
