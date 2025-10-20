# Internal Reviews

Before seeking feedback from other teams, we conducted an internal review of the Personal Expense Tracker to identify areas for improvement and implement initial changes.

**Click on the links below to go to the associated review.**

- [Review 1: test_app.py](#review-1-test_apppy) (_reviewed by Brando_)
- [Review 2: app.py](#review-2-apppy) (_reviewed by Brando_)

## Review 1: `test_app.py`

- **Date received:** 05/10/2025
- **Purpose:** Feedback for this file focused on improving the clarity and completeness of the test function docstrings.
- **Outcome:** The feedback has been considered, and the docstrings in `test_app.py` have been updated to provide further detail. See the “Updated docstring” section under each test below for the specific changes implemented.

---

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

**Updated docstring:**

```python
def test_transaction_creation_expense():
    """Verify that an expense transaction is created with correct attributes and is recognised as an expense."""
```

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

**Updated docstring:**

```python
def test_transaction_creation_expense():
    """Verify that an income transaction is created with correct attributes and is recognised as income."""
```

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

**Updated docstring:**

```python
def test_transaction_creation_expense():
    """Ensure transactions default to "expense" when no type is specified, and related checks behave consistently."""
```

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

**Updated docstring:**

```python
def test_transaction_creation_expense():
    """Check that income returns a positive signed amount and expenses return a negative signed amount, ensuring accurate balance calculations."""
```

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

**Updated docstring:**

```python
def test_transaction_creation_expense():
    """Verify that invalid date formats raise a ValueError indicating the required DD/MM/YYYY format."""
```

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

**Updated docstring:**

```python
def test_transaction_creation_expense():
    """Confirm that invalid transaction types raise a ValueError, enforcing only "income" or "expense" as valid options."""
```

---

## Review 2: `app.py`

- **Date received:** 19/10/2025
- **Purpose:** Feedback for this file focused on improving the clarity and completeness of the main application's docstrings.
- **Outcome:** The feedback has been considered, and the docstrings in `app.py` have been updated to provide further detail. See the “Updated docstring” section under each test below for the specific changes implemented.

---

#### 1. `class Transaction: def __init__`

**Original code:**

```python
class Transaction:
    """Class to represent a financial transaction"""

    def __init__(self, date: str, category: str, description: str, amount: float, transaction_type: str = "expense"):
        self.date = self._validate_date(date)
        self.category = category.strip().title()
        self.description = description.strip()
        self.amount = abs(float(amount))
        self.transaction_type = transaction_type.lower()

        # Validate transaction type
        if self.transaction_type not in ["income", "expense"]:
            raise ValueError("Transaction type must be 'income' or 'expense'")
```

**Suggested improvement:**

```python
"""
Class to represent a financial transaction, such as an income or expense entry.
Attributes:
    date (str): The date of the transaction in DD/MM/YYYY format.
    category (str): The category the transaction belongs to (e.g., Food, Salary).
    description (str): A short description of the transaction.
    amount (float): The value of the transaction amount.
    transaction_type (str): Either 'income' or 'expense'.
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 2. `class Transaction: def _validate_date`

**Original code:**

```python
class Transaction:

    ...

    def _validate_date(self, date_str: str) -> str:
        """Validate and format date string in the format DD/MM/YYYY"""
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return date_str
        except ValueError:
            raise ValueError("Date must be in DD/MM/YYYY format")
```

**Suggested improvement:**

```python
"""
Validate that a date string is in correct format.

Arguments:
    date_str (str): The date string to validate.
Returns:
    The validated and formatted date string in DD/MM/YYYY format.
Raises:
    ValueError: If the date format is invalid.
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 3. `class Transaction: def get_signed_amount`

**Original code:**

```python
class Transaction:

    ...

    def get_signed_amount(self) -> float:
        """Return amount with proper sign: positive (+) for income or negative (-) for expense"""
        return self.amount if self.transaction_type == "income" else -self.amount
```

**Suggested improvement:**

```python
"""
Return the transaction amount with correct sign based on transaction type.

Returns:
    float: Positive value for income, negative value for expense.
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 4. `class Transaction: def is_income`

**Original code:**

```python
class Transaction:

    ...

    def is_income(self) -> bool:
        """Check if this is an income transaction"""
        return self.transaction_type == "income"
```

**Suggested improvement:**

```python
"""
Validate that transaction type equals ‘income’.
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 5. `class Transaction: def is_expense`

**Original code:**

```python
class Transaction:

    ...

    def is_expense(self) -> bool:
        """Check if this is an expense transaction"""
        return self.transaction_type == "expense"
```

**Suggested improvement:**

```python
"""
Validate that transaction type equals ‘expense’.
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 6. `class Transaction: def to_list`

**Original code:**

```python
class Transaction:

    ...

    def to_list(self) -> List:
        """Convert transaction to list format for storage in CSV"""
        return [self.date, self.category, self.description, self.amount, self.transaction_type]
```

**Suggested improvement:**

```python
"""
Convert transaction to list format for CSV storage
Returns:
    List: [date, category, description, amount, transaction_type]
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 7. `class Transaction: def to_dict`

**Original code:**

```python
class Transaction:

    ...

    def to_dict(self) -> Dict:
        """Convert transaction to dictionary format"""
        return {
            'date': self.date,
            'category': self.category,
            'description': self.description,
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'signed_amount': self.get_signed_amount()
        }
```

**Suggested improvement:**

```python
"""
Convert transaction to dictionary format for analysis

Returns:
    Dict: {
        'date': str,
        'category': str,
        'description': str,
        'amount': float,
        'transaction_type': str,
        'signed_amount': float
    }
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 8. `class Transaction: def __str__`

**Original code:**

```python
class Transaction:

    ...

    def __str__(self) -> str:
        """String representation of transaction"""
        sign = "+" if self.is_income() else "-"
        return f"{self.date} | {self.category} | {self.description} | {sign}${self.amount:.2f}"
```

**Suggested improvement:**

```python
"""
Transaction details formatted as a string
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 9. `class ExpenseTracker: def __init__`

**Original code:**

```python
class ExpenseTracker:
    """Main class to manage expense tracking functionality"""

    def __init__(self, csv_file: str = "transactions.csv"):
        self.csv_file = csv_file
        self.transactions: List[Transaction] = []
        self.csv_headers = ["date", "category", "description", "amount", "transaction_type"]

        # Load existing transactions on startup
        self.load_transactions()
```

**Suggested improvement:**

```python
"""
This class uses composition — it contains multiple Transaction instances
and provides functionality for saving, loading, filtering, and summarizing them.

Attributes:
    csv_file (str): The filename used for data storage.
    transactions (List[Transaction]): List of all transactions in memory.
    csv_headers (List[str]): Column headers for CSV export.
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 10. `class ExpenseTracker: def add_transaction`

**Original code:**

```python
class ExpenseTracker:

    ...

    def add_transaction(self, transaction: Transaction) -> None:
        """Add a new transaction to the tracker"""
        self.transactions.append(transaction)
        self.save_transactions()
```

**Suggested improvement:**

```python
"""
Adds a new transaction and inputs it to the CSV file.

Arguments:
    transaction (Transaction): The transaction object to add.

Actions:
    Writes the updated transaction list to the CSV file.
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 11. `class ExpenseTracker: def load_transactions`

**Original code:**

```python
class ExpenseTracker:

    ...

    def load_transactions(self) -> None:
        """Load transactions from CSV file"""
        try:
            if os.path.exists(self.csv_file):
                with open(self.csv_file, 'r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        try:
                            transaction = Transaction(
                                date=row['date'],
                                category=row['category'],
                                description=row['description'],
                                amount=float(row['amount']),
                                transaction_type=row['transaction_type']
                            )
                            self.transactions.append(transaction)
                        except (ValueError, KeyError) as e:
                            print(f"Warning: Skipping invalid transaction in CSV: {e}")
                            continue
                print("\n" + "=" * 50 + "\n")
                print(f"Loaded {len(self.transactions)} transactions from {self.csv_file}" + "\n")
            else:
                print(f"No existing data file found. Now creating a new file...")
        except Exception as e:
            print(f"Error loading transactions: {e}")
```

**Suggested improvement:**

```python
"""
Loads transactions from the CSV file into memory.

Reads each row, creates a Transaction instance, and appends it to `self.transactions`.
Skips rows that fail validation.

Actions:
    Prints loading status and warnings to the console.
    Modifies `self.transactions` in-place.
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 12. `class ExpenseTracker: def get_summary_stats`

**Original code:**

```python
class ExpenseTracker:

    ...

    def get_summary_stats(self) -> Dict:
        """Get summary statistics"""
        if not self.transactions:
            return {
                'total_transactions': 0,
                'total_income': 0,
                'total_expenses': 0,
                'net_balance': 0,
                'categories': []
            }

        income_transactions = self.get_transactions_by_type("income")
        expense_transactions = self.get_transactions_by_type("expense")

        total_income = sum(t.amount for t in income_transactions)
        total_expenses = sum(t.amount for t in expense_transactions)

        return {
            'total_transactions': len(self.transactions),
            'total_income': total_income,
            'total_expenses': total_expenses,
            'net_balance': total_income - total_expenses,
            'categories': self.get_categories()
        }
```

**Suggested improvement:**

```python
"""
Compute overall summary of all transactions.

Returns:
    Dict: {
        'total_transactions': int,
        'total_income': float,
        'total_expenses': float,
        'net_balance': float,
        'categories': List[str]
    }
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 13. `class ExpenseTrackerCLI: def display_transactions`

**Original code:**

```python
class ExpenseTrackerCLI:

    ...

    def display_transactions(self, transactions: List[Transaction], title: str = "Transactions") -> None:
        """Display transactions in a formatted table"""
        if not transactions:
            print(f"\n{title}")
            print("No transactions found.")
            return
    ...
```

**Suggested improvement:**

```python
"""
Display a list of transactions in a formatted table using tabulate.

Arguments:
    transactions (List[Transaction]): List of transactions to display.
    title (str, optional): Header title for the display. Defaults to "Transactions".

Returns:
    None
"""
```

**Updated docstring:**

```python
# WIP
```

---

#### 14. `class ExpenseTrackerCLI: def run`

**Original code:**

```python
class ExpenseTrackerCLI:

    ...

    def run(self) -> None:
        """Main application loop"""
        print("Welcome to the Personal Expense Tracker!")

    ...
```

**Suggested improvement:**

```python
"""
Initialise the interactive CLI loop for the Expense Tracker.

Continuously displays the main menu until the user exits.
Handles keyboard interrupts gracefully and saves data before exiting.
"""
```

**Updated docstring:**

```python
# WIP
```

---
