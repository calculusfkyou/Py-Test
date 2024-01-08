n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())
    if (d - c) == (c - b):
        print(a, b, c, d, d * 2 - c)
    else:
        print(a, b, c, d, (d * d / c))
