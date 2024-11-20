from django.db import models


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Доход'),
        ('expense', 'Расход'),
    )
    title = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)
