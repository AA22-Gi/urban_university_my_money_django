from django.db import models


class Transaction(models.Model):
    """
    Модель для представления финансовых транзакции.

    Атрибуты:
        title (str): Описание транзакции.
        amount (float): Сумма транзакции (максимум 10 цифр, 2 из которых после запятой).
        transaction_type (str): Тип транзакции (может быть 'income' (Доход) или 'expense' (Расход)).
        date (DateField): Дата создания транзакции (устанавливается автоматически при добавлении).
    """

    TRANSACTION_TYPES = (
        ('income', 'Доход'),
        ('expense', 'Расход'),
    )
    title = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'