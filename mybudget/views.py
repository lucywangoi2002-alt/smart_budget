from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Category, Income, Expense
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, ExpenseForm, IncomeForm
from django.db.models import Sum
from django.contrib import messages
import json


@login_required
def add_income(request):

    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user   # attach logged-in user
            income.save()

            messages.success(request, 'Income added successfully!')

            return redirect('dashboard')
    else:
        form = IncomeForm()

    return render(request, 'add_income.html', {'form': form})



@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('add_expense')
    else:
        # Filter categories to only those owned by logged-in user
        form = ExpenseForm()
        form.fields['category'].queryset = Category.objects.filter(user=request.user)
        return render(request, 'add_expenses.html', {'form': form})

    return render(request, 'add_expenses.html', {'form': form})

@login_required
def view_expenses(request):
    user = request.user
    expenses = Expense.objects.all().filter(user=user)
    return render(request, 'view_expenses.html', {'expenses': expenses})

login_required
def view_incomes(request):
    user = request.user
    incomes = Income.objects.all().filter(user=user)
    return render(request, 'view_incomes.html', {'incomes': incomes})

@login_required
def view_categories(request):
    user = request.user
    categories = Category.objects.filter(user=user)
    return render(request, 'view_categories.html', {'categories': categories})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'Category added successfully!')
            return redirect('add_category')
    else:
        form = CategoryForm()
        redirect('add_category')

    return render(request, 'add_category.html', {'form': form})



@login_required
def dashboard(request):
    user = request.user

    incomes = Income.objects.filter(user=user)
    expenses = Expense.objects.filter(user=user)

    total_income = float(sum([inc.amount for inc in incomes]))
    total_expense = float(sum([exp.amount for exp in expenses]))
    balance = total_income - total_expense

    categories = []
    category_totals = []

    for cat in Category.objects.filter(user=user):
        total = sum(exp.amount for exp in expenses if exp.category == cat)
        if total > 0:
            categories.append(cat.name)
            category_totals.append(float(total))  # convert Decimal to float

    if category_totals:
        max_index = category_totals.index(max(category_totals))
        top_category = categories[max_index]
        category_percent = round(category_totals[max_index] / total_expense * 100, 2)
    else:
        top_category = None
        category_percent = None



    context = {
        'total_income': float(total_income),
        'total_expense': float(total_expense),
        'balance': float(balance),
        'categories_json': json.dumps(categories),
        'category_totals_json': json.dumps(category_totals),
        'top_category': top_category,
        'category_percent': category_percent,
        'analysis': "Your expenses exceed your income. Consider reviewing your spending habits." if balance < 0 else "Your income and expenses are balanced. Keep monitoring to maintain this!" if balance == 0 else "Great job! Your income exceeds your expenses. Consider saving or investing the surplus."
    }

    return render(request, 'dashboard.html', context)

def reset_data(request):
    if request.method == 'POST':
        user = request.user
        Income.objects.filter(user=user).delete()
        Expense.objects.filter(user=user).delete()
        Category.objects.filter(user=user).delete()
        messages.success(request, 'All your data has been reset successfully!')
        return redirect('dashboard')