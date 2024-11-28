from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    """
    Форма для создания и редактирования транзакции.

    Эта форма основана на модели `Transaction` и позволяет пользователю
    вводить данные для названия, суммы и типа транзакции.

    Атрибуты:
        Meta (class): Внутренний класс, определяющий модель, поля и метки.
    """

    class Meta:
        model = Transaction  # Модель, к которой относится форма
        fields = ['title', 'amount', 'transaction_type']  # Поля для ввода данных
        labels = {
            'title': 'Название',  # Метка для поля названия
            'amount': 'Сумма',  # Метка для поля суммы
            'transaction_type': 'Тип транзакции',  # Метка для поля типа транзакции
        }