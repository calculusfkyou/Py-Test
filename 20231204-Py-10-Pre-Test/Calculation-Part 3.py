# a,b = input().split(), input().split(); (lambda a, b: print(int(eval(''.join([a[i] + (b[i] if(b[i] != '/') else '//') if(i != len(b)) else a[i] for i in range(len(a))])))))(a, (b + b*((len(a)//len(b))))[:len(a)-1])

nums = list(map(int, input().split()))
operands = list(map(str, input().split()))
t, temp = [], 0
for i in range(len(nums)):
    t.append(str(nums[i]))
    if temp == len(operands):
        temp = 0
    if operands[temp]=="/":
        t.append("//")
    else:
        t.append(operands[temp])
    temp += 1
t.pop()
print(eval("".join(t)))