"""
Shopping Cart System
--------------------
Demonstrates OOP principles with Product, Cart, and interaction logic 
for managing items, calculating totals, and applying discounts.
"""

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


class ShoppingCart:
    def __init__(self):
        # Dictionary mapping Product object to quantity
        self.items = {}

    def add_item(self, product, quantity=1):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        
        if product.stock < quantity:
            print(f"Sorry, only {product.stock} units of {product.name} available.")
            return
            
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
            
        product.stock -= quantity
        print(f"Added {quantity}x {product.name} to your cart.")

    def remove_item(self, product, quantity=1):
        if product in self.items:
            if quantity >= self.items[product]:
                product.stock += self.items[product]
                del self.items[product]
                print(f"Removed all {product.name} from cart.")
            else:
                self.items[product] -= quantity
                product.stock += quantity
                print(f"Removed {quantity}x {product.name} from cart.")
        else:
            print("Item not found in cart.")

    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.items.items())

    def view_cart(self):
        if not self.items:
            print("\nYour shopping cart is empty.")
            return
            
        print("\n--- YOUR SHOPPING CART ---")
        for product, qty in self.items.items():
            subtotal = product.price * qty
            print(f"- {product.name} x {qty} @ ${product.price:.2f} = ${subtotal:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
        print("--------------------------")


def main():
    # Setup inventory
    p1 = Product("Laptop", 999.99, 5)
    p2 = Product("Mouse", 25.50, 20)
    p3 = Product("Keyboard", 45.00, 10)
    
    catalog = [p1, p2, p3]
    cart = ShoppingCart()
    
    while True:
        print("\n=== E-COMMERCE STORE ===")
        print("1. View Products")
        print("2. View Cart")
        print("3. Add Item to Cart")
        print("4. Remove Item from Cart")
        print("5. Checkout & Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == "1":
            print("\n--- AVAILABLE PRODUCTS ---")
            for idx, prod in enumerate(catalog, 1):
                print(f"{idx}. {prod}")
                
        elif choice == "2":
            cart.view_cart()
            
        elif choice == "3":
            try:
                idx = int(input("Enter product number to add: ")) - 1
                if 0 <= idx < len(catalog):
                    qty = int(input("Enter quantity: "))
                    cart.add_item(catalog[idx], qty)
                else:
                    print("Invalid product selection.")
            except ValueError:
                print("Please enter valid numeric inputs.")
                
        elif choice == "4":
            try:
                idx = int(input("Enter product number to remove from cart: ")) - 1
                if 0 <= idx < len(catalog):
                    qty = int(input("Enter quantity to remove: "))
                    cart.remove_item(catalog[idx], qty)
                else:
                    print("Invalid product selection.")
            except ValueError:
                print("Please enter valid numeric inputs.")
                
        elif choice == "5":
            cart.view_cart()
            print("\nThank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()
