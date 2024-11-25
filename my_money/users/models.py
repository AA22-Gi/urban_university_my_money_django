from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)  # Имя
    surname = models.CharField(max_length=100)  # Фамилия
    age = models.PositiveIntegerField(null=True)  # Возраст
    gender = models.CharField(max_length=10)  # Пол
    email = models.EmailField(unique=True)  # Почта
    password = models.CharField(max_length=128) # Пароль

    def __str__(self):
        return f"{self.name} {self.surname}"


