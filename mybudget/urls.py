from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-income/', views.add_income, name='add_income'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-category/', views.add_category, name='add_category'),
    path('reset-data/', views.reset_data, name='reset_data'),
    path('view-expenses/', views.view_expenses, name='view_expenses'),
    path('view-incomes/', views.view_incomes, name='view_incomes'),
    path('view-categories/', views.view_categories, name='view_categories'),
]