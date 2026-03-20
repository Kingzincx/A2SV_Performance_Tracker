n, k = map(int, input().split())
ls = sorted(list(map(int, input().split())))

if k == 0:
    if ls[0] == 1:
        print(-1)
    else:
        print(1)
else:
    x = ls[k - 1]
    
    if k < n and ls[k] == x:
        print(-1)
    else:
        print(x + 1)