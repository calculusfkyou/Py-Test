# 測茲沒有空格
n = int(input())
m = int(input())
for i in range(1, n + 1):
    print(" ".join(str(i) * i))
print()
for i in range(-m, 0, -1):
    print(" ".join(str(i) * i))
