import string

def is_palindrome(text):
    # Remove punctuation and spaces, and convert to lowercase
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    user_input = input("Enter a word or phrase to check for a palindrome: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")
