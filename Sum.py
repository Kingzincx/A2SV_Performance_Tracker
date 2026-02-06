t = int(input())

for i in range(t):
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    if (a + b == c):
        print("YES")
    elif (b + c == a):
        print("YES")
    elif (a + c == b):
        print("YES")
    else:
        print("NO")