while True:
    try:
        n = int(input())
        for i in range(1, n + 1):
            if i == n:
                print('.' * (n + n - 1))
            elif i == 1:
                print(' ' * (n - 1) + '.')
            else:
                print(' ' * (n - i) + '.' + ' ' * (2 * (i - 1) - 1) + '.')
    except:
        break
