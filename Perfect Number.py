n = int(input("Enter number: "))
total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print("Perfect number")
else:
    print("Not a Perfect number")
