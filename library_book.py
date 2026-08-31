class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"You have checked out '{self.title}' by {self.author}."
        return f"'{self.title}' is already checked out."

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"Thank you for returning '{self.title}'."
        return f"'{self.title}' was not checked out."

# Creating an object
my_book = Book("1984", "George Orwell")

# Interacting with the object
print(my_book.check_out())      # Output: You have checked out '1984' by George Orwell.
print(my_book.check_out())      # Output: '1984' is already checked out.
print(my_book.return_book())    # Output: Thank you for returning '1984'.
