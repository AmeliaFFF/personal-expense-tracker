# Internal Review

Before seeking feedback from other teams, we conducted an internal review of the Personal Expense Tracker to identify areas for improvement and implement initial changes.

**Review of the below files was provided by Brando.**

## `test_app.py`

The feedback given for this file focuses specifically on the clarity and completeness of the docstrings.

#### 1. `test_transaction_creation_expense()`

**Original code:**

```python
def test_transaction_creation_expense():
    """Test for creating a basic expense transaction"""
    transaction = Transaction("01/07/2025", "Food", "Lunch at cafe", 15.50, "expense")

    assert transaction.date == "01/07/2025"
    assert transaction.category == "Food"
    assert transaction.description == "Lunch at cafe"
    assert transaction.amount == 15.50
    assert transaction.is_expense() == True
```

**Suggested improvement:**

- This test validates that an expense transaction is created correctly.
- This test ensures that when an expense transaction is created:
  - Attributes (date, category, description, amount) are stored correctly
  - The transaction categorises itself as an expense using ‘is_expense()’

---

#### 2. `test_transaction_creation_income()`

**Original code:**

```python
def test_transaction_creation_income():
    """Test for creating a basic income transaction"""
    transaction = Transaction("14/07/2025", "Wages", "Pay from work", 1000.00, "income")

    assert transaction.date == "14/07/2025"
    assert transaction.category == "Wages"
    assert transaction.description == "Pay from work"
    assert transaction.amount == 1000.00
    assert transaction.is_income() == True
```

**Suggested improvement:**

- This test validates that an income transaction is created correctly.
- This test ensures that when an income transaction is created:
  - Attributes (date, category, description, amount) are stored correctly
  - The transaction categorises itself as an income using ‘is_income()

---

#### 3. `test_transaction_default_type()`

**Original code:**

```python
def test_transaction_default_type():
    """Test that default transaction type is expense"""
    transaction = Transaction("02/07/2025", "Takeaway", "Coffee", 7.50)

    assert transaction.transaction_type == "expense"
    assert transaction.is_expense() == True
    assert transaction.is_income() == False
```

**Suggested improvement:**

- This test validates that transactions default to 'expense' when no type is specified.
- This ensures the Transaction class assigns 'expense' as the default type and that (is_expense / is_income) behave consistently.

---

#### 4. `test_transaction_signed_amount()`

**Original code:**

```python
def test_transaction_signed_amount():
    """Test that signed amounts work correctly for income(+) and expense(-) transactions"""
    income = Transaction("14/06/2025", "Wages", "Pay from work", 1000.00, "income")
    assert income.get_signed_amount() == +1000.00

    expense = Transaction("03/08/2025", "Bills", "Phone bill", 73.00, "expense")
    assert expense.get_signed_amount() == -73.00
```

**Suggested improvement:**

- This test validates that correct signs are returned for income (+) and expense (-) transactions.
  - Income transactions return a positive value.
  - Expense transactions return a negative value.
- This is crucial for accurate balance calculations.

---

#### 5. `test_transaction_invalid_date()`

**Original code:**

```python
def test_transaction_invalid_date():
    """Test that invalid date formats raise an error"""
    with pytest.raises(ValueError, match="Date must be in DD/MM/YYYY format"):
        Transaction("2025-01-25", "Food", "Restaurant dinner", 37.80, "expense")
```

**Suggested improvement:**

- This test confirms that invalid date formats are rejected.
- This test should raise a ValueError when the date is not provided in the expected 'DD/MM/YYYY' format.

---

#### 6. `test_transaction_invalid_type()`

**Original code:**

```python
def test_transaction_invalid_type():
    """Test that invalid transaction types raise an error"""
    with pytest.raises(ValueError, match="Transaction type must be 'income' or 'expense'"):
        Transaction("31/07/2025", "Groceries", "Shopping for dinner", 34.56, "food")
```

**Suggested improvement:**

- This test confirms that invalid transaction types raise a ValueError.
- The Transaction class should only accept 'income' or 'expense'. Any other value should trigger a ValueError to prevent invalid data.

---
