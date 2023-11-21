try:
    while (True):
        n = input()
        t = 0
        if n == ' ':
            print(' \n')
            continue
        for i in n:
            if i.isdigit():
                t += int(i)
                continue
            if i == '!':
                print()
                continue
            if i == 'b':
                print(' ' * t, end='')
            else:
                print(i * t, end='')
            t = 0
        print()
except Exception as e:
    pass
