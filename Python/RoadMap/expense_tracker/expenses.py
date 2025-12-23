import register 

from datetime import datetime
from typing import Optional

def valid_inputs(value, string, month: Optional[int] = None):
    if value <= 0:
        raise ValueError("Amount must be greater than 0")
    if string == "":
        raise ValueError("Description cannot be empty")
    if month is not None:
        if int(month) > 12 and int(month) < 1:
            raise ValueError("Month must be between 1 and 12")
    return True

def create_expense(description, amount):
    if valid_inputs(amount, description):
        register_date = datetime.now().strftime('%Y-%m-%d')
        create = register.register_create(description, amount, register_date)
        return "Expense created successfully with id: " + str(create)
    
def update_expense(id, description, amount):
    if valid_inputs(amount, description):
        register.register_update(id, description, amount)
    return "Expense updated successfully"
    
def delete_expense(id):
    register.register_delete(id)
    return "Expense deleted successfully"

def list_expenses(month=None):
    expenses = register.list_expenses()
    formatted_expenses = []
    for expense in expenses:
        current_month = datetime.now().month
        register_month = datetime.strptime(expense['date'], '%Y-%m-%d').month
        if month is not None:
            if register_month == month:
                formatted_expense = {
                    'id': expense['id'],
                    'description': expense['description'],
                    'date': expense['date'],
                    'amount': expense['amount']
                }
            if register_month == current_month:
                formatted_expense = {
                    'id': expense['id'],
                    'description': expense['description'],
                    'date': register_month,
                    'amount': expense['amount']
                }
        formatted_expenses.append(formatted_expense)
    return formatted_expenses
        

def total_expenses(month=None):
    expenses = register.list_expenses()
    total = 0
    total_month = 0
    for expense in expenses:
        if month is not None:
            month_string = f"2025-{month}-01"
            month_datetime = datetime.strptime(month_string, '%Y-%m-%d')
            register_month = datetime.strptime(expense['date'], '%Y-%m-%d')
            month_name = register_month.strftime('%B')
            if register_month.month == month_datetime.month:
                total_month += float(expense['amount'])
        else:
            total += float(expense['amount'])
    if month is not None:
        return "Total expenses in " + month_name + ": $" + str(total_month)
    return "Total expenses: $" + str(total)