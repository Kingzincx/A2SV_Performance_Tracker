r = c = 0
for i in range(1, 6):
    row = list(map(int, input().split()))
    for j, x in enumerate(row, start=1):
        if x == 1:
            r, c = i, j
print(abs(r - 3) + abs(c - 3))