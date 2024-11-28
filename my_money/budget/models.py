from django.db import models
from users.models import User


class Transaction(models.Model):
    """
    Модель транзакции.

    Эта модель представляет транзакцию, которая может быть либо
    доходом, либо расходом. Она содержит информацию о названии,
    сумме, типе транзакции, дате и привязанному пользователю.

    Атрибуты:
        title (str): Название транзакции.
        amount (Decimal): Сумма транзакции.
        transaction_type (str): Тип транзакции (доход или расход).
        date (DateField): Дата создания транзакции (автоматически устанавливается).
        user (ForeignKey): Связанный пользователь (пользователь, создавший транзакцию).
    """

    TRANSACTION_TYPES = (
        ('income', 'Доход'),
        ('expense', 'Расход'),
    )

    title = models.CharField(max_length=30)  # Название транзакции
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма транзакции
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)  # Тип транзакции
    date = models.DateField(auto_now_add=True)  # Дата создания транзакции
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, создавший транзакцию

    def __str__(self):
        """
        Возвращает строковое представление транзакции.
        """
        return f'{self.title}'