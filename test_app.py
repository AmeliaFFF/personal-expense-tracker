import pytest
from app import Transaction, ExpenseTracker, ExpenseTrackerCLI
from datetime import datetime

def test_transaction_creation_expense():
    """Verify that an expense transaction is created with correct attributes and is recognised as an expense."""
    transaction = Transaction("01/07/2025", "Food", "Lunch at cafe", 15.50, "expense")
    
    assert transaction.date == "01/07/2025"
    assert transaction.category == "Food"
    assert transaction.description == "Lunch at cafe"
    assert transaction.amount == 15.50
    assert transaction.is_expense() == True

def test_transaction_creation_income():
    """Verify that an income transaction is created with correct attributes and is recognised as income."""
    transaction = Transaction("14/07/2025", "Wages", "Pay from work", 1000.00, "income")
    
    assert transaction.date == "14/07/2025"
    assert transaction.category == "Wages"
    assert transaction.description == "Pay from work"
    assert transaction.amount == 1000.00
    assert transaction.is_income() == True

def test_transaction_default_type():
    """Ensure transactions default to "expense" when no type is specified, and related checks behave consistently."""
    transaction = Transaction("02/07/2025", "Takeaway", "Coffee", 7.50)
    
    assert transaction.transaction_type == "expense"
    assert transaction.is_expense() == True
    assert transaction.is_income() == False

def test_transaction_signed_amount():
    """Check that income returns a positive signed amount and expenses return a negative signed amount, ensuring accurate balance calculations."""
    income = Transaction("14/06/2025", "Wages", "Pay from work", 1000.00, "income")
    assert income.get_signed_amount() == +1000.00
    
    expense = Transaction("03/08/2025", "Bills", "Phone bill", 73.00, "expense")
    assert expense.get_signed_amount() == -73.00

def test_transaction_invalid_date():
    """Verify that invalid date formats raise a ValueError indicating the required DD/MM/YYYY format."""
    with pytest.raises(ValueError, match="Date must be in DD/MM/YYYY format"):
        Transaction("2025-01-25", "Food", "Restaurant dinner", 37.80, "expense")

def test_transaction_invalid_type():
    """Confirm that invalid transaction types raise a ValueError, enforcing only "income" or "expense" as valid options."""
    with pytest.raises(ValueError, match="Transaction type must be 'income' or 'expense'"):
        Transaction("31/07/2025", "Groceries", "Shopping for dinner", 34.56, "food")