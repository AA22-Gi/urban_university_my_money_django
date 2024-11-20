from django.db import models

class Transaction(models.Model):
    title = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)