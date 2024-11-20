from django.shortcuts import render


def  transaction_dashboard(request):
    return render(request, 'templates/transaction_dashboard.html')
