from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser ):
    GENDER_CHOICES = [('M', 'мужской'), ('F', 'женский')]

    # Поля, которые вы хотите оставить
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)


    # Переопределяем поля first_name и last_name, чтобы они не использовались
    first_name = None
    last_name = None
