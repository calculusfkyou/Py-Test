nums = list(map(int, input().split()))
operands = list(map(str, input().split()))
t, temp = [], 0
for i in range(len(nums)):
    t.append(nums[i])
    if temp == len(operands):
        temp = 0
    t.append(operands[temp])
    temp += 1
# print(t)
t.pop()
temp, check = [], 1
for i in range(len(t)):
    if not check:
        check = 1
        continue
    if t[i] == "*":
        temp.append(temp[-1] * t[i + 1])
        temp.pop(-2)
        check = 0
    elif t[i] == "/":
        temp.append(temp[-1] // t[i + 1])
        temp.pop(-2)
        check = 0
    elif t[i] == "%":
        temp.append(temp[-1] % t[i + 1])
        temp.pop(-2)
        check = 0
    else:
        temp.append(t[i])
# print(temp)
ans = []
for i in range(len(temp)):
    if not check:
        check = 1
        continue
    if temp[i] == "+":
        ans.append(ans[-1] + temp[i + 1])
        ans.pop(-2)
        check = 0
    elif temp[i] == "-":
        ans.append(ans[-1] - temp[i + 1])
        ans.pop(-2)
        check = 0
    else:
        ans.append(temp[i])
print(int(ans[0]))