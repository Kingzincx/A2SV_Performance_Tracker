n = int(input())

for _ in range(n):
    st = input()
    if len(st) > 10:
        print(st[0], len(st) - 2, st[-1],sep="")
    else:
        print(st)