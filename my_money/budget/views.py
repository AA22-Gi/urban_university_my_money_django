from django.shortcuts import render


def  transaction_dashboard(request):
    return render(request, 'budget/transaction_dashboard.html')
