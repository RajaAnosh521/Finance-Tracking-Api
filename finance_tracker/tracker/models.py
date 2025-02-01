from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Category(models.Model):
    user = models.CharField(max_length=100) 
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    date = models.DateField(auto_now_add=True)
    transaction_types = [
        ('I', 'Income'),
        ('E', 'Expense'),
    ]
    type = models.CharField(max_length=1, choices=transaction_types) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)