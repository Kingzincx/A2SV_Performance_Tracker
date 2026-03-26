n = int(input())
a = list(map(int, input().split()))

tem_par = False
tem_impar = False

for x in a:
    if x % 2 == 0:
        tem_par = True
    else:
        tem_impar = True

if tem_par and tem_impar:
    a.sort()
print(*a)