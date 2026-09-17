class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})
        print(f"Added ${amount:.2f} under '{category}'.")

    def show_summary(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
            
        total = sum(item["amount"] for item in self.expenses)
        print("\n--- Expense Summary ---")
        for item in self.expenses:
            print(f"- {item['category']}: ${item['amount']:.2f}")
        print(f"Total Spent: ${total:.2f}")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    print("--- Personal Expense Tracker ---")
    
    while True:
        print("\n1. Add Expense\n2. View Summary\n3. Exit")
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            cat = input("Enter category (e.g., Food, Transport): ")
            try:
                amt = float(input("Enter amount ($): "))
                tracker.add_expense(cat, amt)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            tracker.show_summary()
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
