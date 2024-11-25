from django.db import models
from users.models import User


class Transaction(models.Model):
    """
    Модель для представления финансовых транзакции.

    Атрибуты:
        title (str): Описание транзакции.
        amount (float): Сумма транзакции (максимум 10 цифр, 2 из которых после запятой).
        transaction_type (str): Тип транзакции (может быть 'income' (Доход) или 'expense' (Расход)).
        date (DateField): Дата создания транзакции (устанавливается автоматически при добавлении).
        user (User): Пользователь, которому принадлежит транзакция.
    """

    TRANSACTION_TYPES = (
        ('income', 'Доход'),
        ('expense', 'Расход'),
    )
    title = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.title}'
