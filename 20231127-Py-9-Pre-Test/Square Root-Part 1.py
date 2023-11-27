n = list(map(int, input().split()))
if n[0] ** 0.5 - int(n[0] ** 0.5) != 0:
    print(str(n[0] ** 0.5)[n[1] + 1])
else:
    print(0)