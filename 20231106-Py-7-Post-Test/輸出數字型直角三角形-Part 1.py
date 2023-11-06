# 兩種寫法
for i in range(1, int(input()) + 1):
    for j in range(1, i + 1):
        if j != i:
            print(j % 10, end='')
        else:
            print(j % 10, end='\n')

for i in range(1, int(input()) + 1):
    print("".join([str(j % 10) for j in range(1, i + 1)]))
