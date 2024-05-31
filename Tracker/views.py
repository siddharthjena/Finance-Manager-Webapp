from django.shortcuts import render, redirect
from .models import User, Transaction
from decimal import Decimal

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'Tracker/register.html', {'error_message': 'Username already exists'})

        # Create a new user
        user = User.objects.create(username=username, password=password, email=email)
        # Redirect to the login page
        return redirect('login')

    return render(request, 'Tracker/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Retrieve the user from the database based on the provided username
        user = User.objects.filter(username=username).first()

        if user and user.password == password:
            # If the password matches, set a session variable to mark the user as logged in
            request.session['user_id'] = user.id
            # Redirect to the dashboard or a page displaying the name of the logged-in user
            return redirect('home')

    # If the authentication fails, show the login page
    return render(request, 'Tracker/login.html', {'error_message': 'Invalid username or password'})

from datetime import datetime, timedelta

def budget_view(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)

        action = request.POST.get('action')

        if action == 'update_income':
            salary = request.POST.get('salary')
            salary = float(salary) if salary is not None else 0.0
            user.total_inc = user.total_inc or 0  # Ensure total_inc is not None
            user.total_inc += salary
            user.save()
            # Create new Transaction record for income
            Transaction.objects.create(user=user, amount=salary, is_income=True)

        elif action == 'update_expense':
            expense = request.POST.get('expenses')
            mode_of_expense = request.POST.get('mode_of_expense')
            expense = float(expense) if expense is not None else 0.0
            user.total_exp = user.total_exp or 0  # Ensure total_exp is not None
            user.total_exp += expense
            user.save()
            # Create new Transaction record for expense with area
            Transaction.objects.create(user=user, amount=expense, is_income=False, category=mode_of_expense)

        return redirect('dashboard')

    else:
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)

        total_inc = user.total_inc or 0
        total_exp = user.total_exp or 0
        remaining_balance = total_inc - total_exp

        user.remaining = remaining_balance
        user.save()

        return render(request, 'Tracker/dash.html', {'name': user.username, 'remaining_balance': remaining_balance, 'expenses' : total_exp})

def home_view(request):
    user_id = request.session.get('user_id')
    
    
    user = User.objects.get(id=user_id)
    d = {'name': user.username}
    return render(request, 'Tracker/home2.html', d)


def payments(request):
    return render(request,'Tracker/payment.html')