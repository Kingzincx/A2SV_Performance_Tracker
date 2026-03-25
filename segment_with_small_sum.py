n, s = map(int, input().split())
a = list(map(int, input().split()))
i = 0
j = 0
som = 0
res = 0
while j < n:
    som = som + a[j]
    while(som > s):
        som -= a[i]
        i += 1
    res = max(res, j - i + 1)
    j += 1
print(res)