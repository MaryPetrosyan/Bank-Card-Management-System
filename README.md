# 💳 Bank Card Management System

A simple Python-based bank card management system that simulates authentication, deposits, withdrawals, transaction history, and user sessions.

## Features

* Bank card creation
* PIN authentication
* Maximum 3 login attempts
* Automatic card blocking after 3 failed PIN entries
* Deposit money
* Withdraw money
* Check account balance
* View transaction history
* Logout functionality
* Custom exceptions for card validation

---

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* UUID
* Datetime

---

## Project Structure

```text
project/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## Custom Exceptions

### CardNumberException

Raised when the card number length is not 16 digits.

```python
if len(cardnumber) != 16:
    raise CardNumberException("CardNumber length must be 16")
```

### CvvException

Raised when the CVV length is not 3 digits.

```python
if len(cvv) != 3:
    raise CvvException("cvv length must be 3")
```

---

## How It Works

### Step 1: Create a Bank Card

```python
obj = BankCard(
    "Narine",
    "Vardanyan",
    "1553217320474153",
    "148",
    "1234"
)
```

### Step 2: Login

The user enters their PIN.

```python
obj.make_action()
```

After successful authentication:

* A unique session ID is generated.
* The user is marked as logged in.

### Step 3: Withdraw Money

```python
obj.withdraw(1000)
```

The amount is deducted from the balance and stored in the transaction history.

### Step 4: Deposit Money

```python
obj.deposit(110000)
```

The amount is added to the balance and recorded as a transaction.

### Step 5: Check Balance

```python
print(obj.get_balance())
```

Example output:

```text
Balance : 159000
```

### Step 6: View Transaction History

```python
print(obj.get_transaction())
```

Example output:

```text
2026-07-04 12:30:12 - Withdraw: 1000֏
2026-07-04 12:31:15 - Deposit: 110000֏
```

### Step 7: Logout

```python
obj.logout()
```

The session is terminated and access is revoked.

---

## Running the Program

```bash
python main.py
```

---

## Example Workflow

```text
Enter your pin: 1234

Balance : 159000

2026-07-04 12:30:12 - Withdraw: 1000֏
2026-07-04 12:31:15 - Deposit: 110000֏

Logged out successfully.
```

---

## Key Concepts Demonstrated

* Classes and Objects
* Encapsulation
* Exception Handling
* Session Management
* Transaction Tracking
* Lists and Dictionaries
* UUID Generation
* Date and Time Operations

