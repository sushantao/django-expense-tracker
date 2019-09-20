from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Expense
from .forms import ExpenseForm


def index(request):
    expenses= Expense.objects.all()
    form= ExpenseForm()
    context= {
        'expenses':expenses,
        'form':form,
    }
    return render(request, 'expense/index.html', context)

def add(request):
    form = ExpenseForm(request.POST)
    form.save(commit=True)
    return HttpResponseRedirect(reverse('expense:index'))

def delet(request, id=None):
    expense = get_object_or_404(Expense, pk=id)
    expense.delete()
    return HttpResponseRedirect(reverse('expense:index'))