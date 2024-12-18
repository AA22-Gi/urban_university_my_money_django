from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm


def transaction_dashboard(request):
    """
    Отображает панель управления транзакциями и информацию о балансе пользователя.

    Эта функция берет все транзакции из базы данных, вычисляет общую сумму доходов и расходов,
    а также баланс. Затем она передает собранные данные в контексте для отображения на веб-странице
    через HTML-шаблон.

    Args:
        request (HttpRequest): Объект запроса, содержащий информацию о текущем запросе пользователя.

    Returns:
        HttpResponse: Ответ, содержащий шаблон с контекстом.
    """
    # Получаем транзакции только для текущего пользователя
    transactions = Transaction.objects.filter(user=request.user)
    all_income = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
    all_expenses = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')
    balance = all_income - all_expenses

    context = {
        'all_transactions': transactions,
        'all_income': all_income,
        'all_expenses': all_expenses,
        'balance': balance
    }

    return render(request, 'budget/transaction_dashboard.html', {'context': context})


def add_transaction(request):
    """
    Обрабатывает добавление новой транзакции.

    Эта функция отображает форму для добавления новой транзакции и сохраняет данные,
    если форма действительна. В случае успешного сохранения происходит перенаправление
    на панель управления транзакциями.

    Args:
        request (HttpRequest): Объект запроса, содержащий информацию о текущем запросе.

    Returns:
        HttpResponse: Ответ с отрендеренным шаблоном 'budget/add_transaction.html',
                      содержащим форму для добавления новой транзакции.
    """
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  # Устанавливаем текущего пользователя
            transaction.save()
            return redirect('transaction_dashboard')
    else:
        form = TransactionForm()

    return render(request, 'budget/add_transaction.html', {'form': form})


def edit_transaction(request, id_transaction):
    """
    Обрабатывает редактирование существующей транзакции.

    Эта функция получает транзакцию по ее идентификатору,
    отображает форму редактирования и сохраняет изменения,
    если форма валидна. В случае успешного сохранения происходит
    перенаправление на панель управления транзакциями.

    Args:
        request (HttpRequest): Объект запроса, содержащий информацию о текущем запросе.
        id_transaction (int): Идентификатор транзакции, которую необходимо редактировать.

    Returns:
        HttpResponse: Ответ с шаблоном 'budget/edit_transaction.html',
                      содержащим форму для редактирования транзакции.
    """
    transaction = get_object_or_404(Transaction, id=id_transaction)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_dashboard')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'budget/edit_transaction.html', {'form': form})


def delete_transaction(request, id_transaction):
    """
    Обрабатывает удаление транзакции.

    Если метод запроса - POST, транзакция с указанным идентификатором
    будет удалена из базы данных, и пользователь будет перенаправлен
    на страницу с информацией о транзакциях. Если метод запроса
    не является POST, будет отображена страница подтверждения удаления
    с информацией о транзакции.

    Args:
        request (HttpRequest): Объект запроса, содержащий информацию о текущем запросе.
        id_transaction (int): Идентификатор транзакции, которую необходимо удалить.

    Returns:
        HttpResponse: Перенаправление на страницу с транзакциями после успешного
                      удаления или рендеринг страницы подтверждения удаления.
    """
    transaction = get_object_or_404(Transaction, id=id_transaction)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_dashboard')

    return render(request, 'budget/delete_transaction.html', {'transaction': transaction})