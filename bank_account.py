class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. Remaining balance: ${self.balance}"
        return "Insufficient funds or invalid amount."

# Creating an object
my_account = BankAccount("Alice", 100.0)

# Interacting with the object
print(my_account.deposit(50))   # Output: Deposited $50. New balance: $150.0
print(my_account.withdraw(30))  # Output: Withdrew $30. Remaining balance: $120.0
print(my_account.withdraw(200)) # Output: Insufficient funds or invalid amount.
