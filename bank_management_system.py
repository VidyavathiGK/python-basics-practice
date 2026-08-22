class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_account(self):
        print("\n----- Account Details -----")
        print("Account Number :", self.account_number)
        print("Holder Name    :", self.holder_name)
        print("Balance        :", self.balance)


# Single Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=4):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print("Interest       :", interest)
        return interest

    def display_account(self):
        super().display_account()
        print("Account Type   : Savings")
        print("Interest Rate  :", self.interest_rate, "%")


# Hierarchical Inheritance
class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=10000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Overdraft limit exceeded.")

    def display_account(self):
        super().display_account()
        print("Account Type   : Current")
        print("Overdraft Limit:", self.overdraft_limit)


# Multilevel Inheritance
class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(
            account_number,
            holder_name,
            balance,
            interest_rate=7
        )
        self.minimum_balance = 5000

    def check_minimum_balance(self):
        if self.balance >= self.minimum_balance:
            print("Minimum balance requirement satisfied.")
        else:
            print("Warning: Minimum balance not maintained.")

    def display_account(self):
        super().display_account()
        print("Account Type   : Premium Savings")
        print("Minimum Balance:", self.minimum_balance)


def main():
    print("===== BANK MANAGEMENT SYSTEM =====")

    savings = SavingsAccount(
        "SA1001",
        "Vidya",
        10000
    )

    current = CurrentAccount(
        "CA1001",
        "Rahul",
        5000
    )

    premium = PremiumSavingsAccount(
        "PA1001",
        "Ananya",
        20000
    )

    # Savings Account
    savings.display_account()
    savings.deposit(2000)
    savings.withdraw(3000)
    savings.calculate_interest()

    # Current Account
    current.display_account()
    current.deposit(5000)
    current.withdraw(12000)

    # Premium Savings Account
    premium.display_account()
    premium.deposit(5000)
    premium.withdraw(4000)
    premium.calculate_interest()
    premium.check_minimum_balance()


if __name__ == "__main__":
    main()
