k, n, w = map(int, input().split())

i = 1
res = 0

while i <= w:
    res += i * k
    i += 1

print(res - n if res > n else 0)