from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'transaction_type']
        labels = {
            'title': 'Название',
            'amount': 'Сумма',
            'transaction_type': 'Тип транзакции',
        }