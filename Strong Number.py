import math

n = int(input("Enter number: "))
temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total += math.factorial(digit)
    temp //= 10

if total == n:
    print("Strong number")
else:
    print("Not a Strong number")
