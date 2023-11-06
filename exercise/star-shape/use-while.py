n = int(input())
# 01
i = 0
while i < n:
    print('*', end='')
    i += 1
print()

# 02
i = 0
while i < n:
    print('*')
    i += 1
print()

# 03~06
i = 1
while i < (n + 1):
    print('*' * i + ' ' * (n - i), end='')
    print(' ' * 3, end='')
    print(' ' * (n - i) + '*' * i, end='')
    print(' ' * 3, end='')
    print('*' * (n - i + 1) + ' ' * (i - 1), end='')
    print(' ' * 3, end='')
    print(' ' * (i - 1) + '*' * (n - i + 1))
    i += 1
print()

# 07~10
i = 1
if n % 2 == 0: n -= 1
while i < (n + 1):
    length = int(abs((n + 1) / 2 - i))
    height = (n + 1) // 2
    if i <= height:
        print(' ' * (height - i) + '*' * (i * 2 - n % 2) + ' ' * (height - i), end='')
        print(' ' * 3, end='')
        print(' ' * (i - 1) + '*' * (n - (i - 1) * 2) + ' ' * (i - 1), end='')
        print(' ' * 3, end='')
    else:
        print(' ' * (n + 3) * 2, end='')
    print('*' * (height - length) + ' ' * length, end='')
    print(' ' * 3, end='')
    print(' ' * length + '*' * (height - length))
    i += 1
print()

# 11~14
i = 1
if n % 2 == 0: n += 1
while i < (n * 2):
    if i <= n:
        print(' ' * (n - i) + '*' * (i * 2 - 1) + ' ' * (n - i), end='')
        print(' ' * 3, end='')
        print(' ' * (i - 1) + '*' * (n * 2 + 1 - i * 2) + ' ' * (i - 1), end='')
        print(' ' * 3, end='')
    else:
        print(' ' * (n * 4 + 4), end='')
    print('*' * (n - abs(n - i)) + ' ' * (abs(n - i)), end='')
    print(' ' * 3, end='')
    print(' ' * (abs(n - i)) + '*' * (n - abs(n - i)))
    i += 1
print()

# 15~18
i = 1
while i < (n * 2):
    if i <= n:
        print(' ' * (n - i) + '* ' * i + ' ' * (n - i), end='')
        print(' ' * 2, end='')
        print(' ' * (i - 1) + '* ' * (n - i + 1) + ' ' * (i - 1), end='')
        print(' ' * 2, end='')
    else:
        print(' ' * (n * 4 + 4), end='')
    for j in range(n):
        if (i + j) % 2 != 0 and j < n - abs(n - i):
            print('*', end='')
        else:
            print(' ', end='')
    print(' ' * 3, end='')
    for j in range(n):
        if (i + j + (n - 1)) % 2 != 0 and j > abs(n - i) - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    i += 1
print()

# 19~22
i = 1
while i < (n * 2):
    if i < n:
        print('*' * i + ' ' * ((n * 2 - 1) - i * 2) + '*' * i, end='')
    else:
        print('*' * (n * 2 - 1), end='')
    print(' ' * 3, end='')
    if i > n:
        print('*' * (n * 2 - i) + ' ' * (i * 2 - (n * 2 + 1)) + '*' * (n * 2 - i), end='')
    else:
        print('*' * (n * 2 - 1), end='')
    print(' ' * 3, end='')
    print(' ' * (n - abs(n - i) - 1) + '*' * (abs(n - i)) + '*' * n, end='')
    print(' ' * 3, end='')
    print('*' * n + '*' * (abs(n - i)) + ' ' * (n - abs(n - i) - 1))
    i += 1
print()

# 23~26
i = 1
while i < (n * 2):
    if i <= n:
        print(' ' * (n - i) + '*' * (i * 2 - 1) + ' ' * (n - i), end='')
    else:
        print('*' * (n * 2 - 1), end='')
    print(' ' * 3, end='')
    if i >= n:
        print(' ' * (i - n) + '*' * ((n * 4 - 1) - i * 2) + ' ' * (i - n), end='')
    else:
        print('*' * (n * 2 - 1), end='')
    print(' ' * 3, end='')
    print('*' * (n - 1) + '*' * (n - abs(n - i)) + ' ' * (abs(n - i)), end='')
    print(' ' * 3, end='')
    print(' ' * (abs(n - i)) + '*' * (n - abs(n - i)) + '*' * (n - 1))
    i += 1
print()
