# 沒寫出來，忘記時間= =
def f():
    return


def copy(arr):
    s = []
    for i in arr:
        s.append(i)
    return s


tree = list(map(eval, input().split()))
node = len(tree)
newtree = []
temp = []

now = 1
maximum = int(tree[-1])

for i in range(len(tree)):
    if int(tree[i]) == now:
        temp.append(tree[i])
    else:
        now += 1
        if len(temp) == 1:
            newtree.extend(temp)
        else:
            temp2 = copy(temp)
            newtree.append(temp2)
        temp.clear()
        temp.append(tree[i])
print(newtree)
print(node)
