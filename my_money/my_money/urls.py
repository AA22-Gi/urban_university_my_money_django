"""
URL configuration for my_money project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from budget.views import transaction_dashboard, edit_transaction, add_transaction, delete_transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', transaction_dashboard, name='transaction_dashboard'),
    path('add_transaction', add_transaction, name='add_transaction'),
    path('edit_transaction/<int:id_transaction>/', edit_transaction, name='edit_transaction'),
    path('delete_transaction/<int:id_transaction>/', delete_transaction, name='delete_transaction'),
]
