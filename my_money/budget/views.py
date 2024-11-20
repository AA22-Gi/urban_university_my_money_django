from django.shortcuts import render
from .models import Transaction


def transaction_dashboard(request):
    """
    Отображает панель управления транзакциями и информацию о балансе пользователя.

    Эта функция берет все транзакции из базы данных, вычисляет общую сумму доходов и расходов, а также баланс.
    Затем она передает собранные данные в контексте для отображения на веб-странице через html-шаблон.

    Параметры:
        request (HttpRequest): Объект запроса, содержащий информацию о текущем запросе пользователя.

    Возвращает:
        HttpResponse: Ответ, содержащий шаблон с контекстом.
    """
    # noinspection PyUnresolvedReferences
    transactions = Transaction.objects.all()
    all_income = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
    all_expenses = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')
    balance = all_income - all_expenses

    context = {'all_transactions': transactions,
               'all_income': all_income,
               'all_expenses': all_expenses,
               'balance': balance}

    return render(request, 'budget/transaction_dashboard.html', {'context': context})
