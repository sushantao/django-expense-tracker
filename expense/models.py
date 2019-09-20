from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
    
class Expense(models.Model):
    expense_item= models.CharField(max_length=20)
    unit= models.IntegerField(default=0)
    amount= models.IntegerField(default=0)

    def __str__(self):
        return self.expense_item
    



