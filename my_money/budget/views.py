from django.shortcuts import render
from .models import Transaction

def  transaction_dashboard(request):
    # noinspection PyUnresolvedReferences
    transactions = Transaction.objects.all()

    return render(request, 'budget/transaction_dashboard.html', {'transactions': transactions})
