from django.urls import path
from .views import transaction_dashboard, edit_transaction, add_transaction, delete_transaction

urlpatterns = [
    path('transaction_dashboard', transaction_dashboard, name='transaction_dashboard'),
    path('add_transaction', add_transaction, name='add_transaction'),
    path('edit_transaction/<int:id_transaction>/', edit_transaction, name='edit_transaction'),
    path('delete_transaction/<int:id_transaction>/', delete_transaction, name='delete_transaction'),
]
