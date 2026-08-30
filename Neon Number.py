n = int(input("Enter a number: "))

square = n * n
total = 0

while square > 0:
    digit = square % 10
    total += digit
    square //= 10

if total == n:
    print("Neon number")
else:
    print("Not a Neon number")
