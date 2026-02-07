import sys

n = int(input().strip())
phone_book = {}

for i in range(n):
    name, number = input().split()
    phone_book[name] = number

for line in sys.stdin:
    q = line.strip()
    if q in phone_book:
        print(f"{q}={phone_book[q]}")
    else:
        print("Not found")
