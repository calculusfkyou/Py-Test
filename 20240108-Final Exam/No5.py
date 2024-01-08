# 期末考沒過，但UVA過了
# UVA10080
# 1
# RCRFCRFFCCRRC
n = int(input())
for i in range(n):
    print(f'Case #{i + 1}:')
    s = input()
    height = (s.count('R'), s.count("F"))
    cl = 0
    f = ["| " for i in range(height[0] + 1)]
    n = ["| " for i in range(height[1] + 1)]
    bottom = '+' + '-' * (len(s) + 2) + '\n'
    for c in s:
        try:
            if cl >= 0:
                if c == 'R':
                    f[cl] = f[cl] + "/"
                    for j in range(len(f)):
                        if j != cl:
                            f[j] = f[j] + " "
                    for k in range(len(n)):
                        n[k] = n[k] + " "
                    cl += 1
                if c == 'C':
                    f[cl] = f[cl] + "_"
                    for j in range(len(f)):
                        if j != cl:
                            f[j] = f[j] + " "
                    for k in range(len(n)):
                        n[k] = n[k] + " "
                if c == 'F':
                    cl -= 1
                    if cl >= 0:
                        f[cl] = f[cl] + "\\"
                        for j in range(len(f)):
                            if j != cl:
                                f[j] = f[j] + " "
                        for k in range(len(n)):
                            n[k] = n[k] + " "
                    else:
                        n[1] = n[1] + "\\"
                        for j in range(len(f)):
                            f[j] = f[j] + " "
                        for k in range(len(n)):
                            if k != 1:
                                n[k] = n[k] + " "
            else:
                if c == 'R':
                    n[-cl] = n[-cl] + "/"
                    for j in range(len(f)):
                        f[j] = f[j] + " "
                    for k in range(len(n)):
                        if k != -cl:
                            n[k] = n[k] + " "
                    cl += 1
                if c == 'C':
                    n[-cl] = n[-cl] + "_"
                    for j in range(len(f)):
                        f[j] = f[j] + " "
                    for k in range(len(n)):
                        if k != -cl:
                            n[k] = n[k] + " "
                if c == 'F':
                    cl -= 1
                    n[-cl] = n[-cl] + "\\"
                    for j in range(len(f)):
                        f[j] = f[j] + " "
                    for k in range(len(n)):
                        if k != -cl:
                            n[k] = n[k] + " "
        except:
            pass
        # print(f)
        # print(n)
    for a in f[::-1]:
        if a.strip() != '|':
            print(a.strip())
    for b in n:
        if b.strip() != '|':
            print(b.strip())
    print(bottom)