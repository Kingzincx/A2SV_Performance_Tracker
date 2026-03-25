n, t = map(int, input().split())
a = list(map(int, input().split()))
i = 0
res = 0
count = 0
for j in range(n):
    count += a[j]
    while count > t:
        count -=a[i]
        i += 1
    res = max(res, j - i + 1)
print(res)