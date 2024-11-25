from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)  # Имя
    age = models.PositiveIntegerField(null=True)  # Возраст
    gender = models.CharField(max_length=10)  # Пол
    email = models.EmailField(unique=True)  # Почта
    password = models.CharField(max_length=128) # Пароль




