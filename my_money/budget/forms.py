from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        labels = {
            'title': 'Название',
            'amount': 'Сумма',
            'transaction_type': 'Тип транзакции',
        }