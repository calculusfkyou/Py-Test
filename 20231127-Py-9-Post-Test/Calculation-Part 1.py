# 不管運算子優先順序
n = list(map(int, input().split()))
x = input().split()
sm = n[0]
for i in range(1, len(n)):
    if x[0] == '+':
        sm += n[i]
    if x[0] == '-':
        sm -= n[i]
    if x[0] == '*':
        sm *= n[i]
    if x[0] == '/':
        sm //= n[i]
    if x[0] == '%':
        sm %= n[i]
    x = x[1:]
print(sm)
