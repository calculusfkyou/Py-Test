def testprint(strs):  # debug用
    print("----------")
    for words in strs:
        print(words)
    print("----------")


n = int(input())

# check：1->odd, 0->even
if n % 2 == 1:
    mid = int(n // 2) + 1  # 中間數
    check = 1
    base = 1
else:
    mid = n // 2
    check = 0
    base = 2

temp = n - 1
s1, s2 = "", ""
while temp >= 0:
    s1 += str(n - temp)
    s2 += str(temp + 1)
    temp -= 1
print(s1 + "   " + s2)
print()

temp = n
while temp > 0:
    print(str(n - temp + 1) + "   " + str(temp))
    temp -= 1
print()

temp = n
mid = n // 2 + 1
while temp > 0:
    s = ""
    s1 = str(n - temp + 1) * (n - temp + 1) + " " * (temp - 1)
    s2 = str(temp) * (n - temp + 1) + " " * (temp - 1)
    s += s1 + "   " + s2 + "   " + s1[::-1] + "   " + s2[::-1] + "   "
    s1 = str(n - temp + 1) * temp + " " * (n - temp)
    s2 = " " * (n - temp) + str(temp) * temp
    s += s1 + "   " + s2 + "   " + s1[::-1] + "   " + s2
    temp -= 1
    print(s)
print()

if not check:
    n -= 1
s1, s2, s5, s6 = [], [], [], []
s3, s4 = [], []
i, temp = 1, n
s, ss = "", ""
c = 1
while i <= n:
    s1.append(" " * ((n - i) // 2) + str(i) * i + " " * ((n - i) // 2))
    s2.append(" " * ((n - i) // 2) + str(temp) * i + " " * ((n - i) // 2))
    s += str(temp)
    s5.append(s + " " * (n // 2 + 1 - c))
    ss += str(i)
    s6.append(ss + " " * (n // 2 + 1 - c))
    temp -= 2
    c += 1
    i += 2
s3 = s1[::-1]
s4 = s2[::-1]
s5 += s5[:-1][::-1]
s6 += s6[:-1][::-1]
i = n - len(s1)
while i > 0:
    s1.append(" " * n)
    s2.append(" " * n)
    s3.append(" " * n)
    s4.append(" " * n)
    i -= 1
i = 0
while i < n:
    print(s1[i] + "   " + s2[i] + "   " + s3[i] + "   " + s4[i] + "   " + s5[i] + "   " + s6[i] + "   " +
          s5[i][::-1] + "   " + s6[i][::-1])
    i += 1
print()

if not check:
    n += 1
s1, s2, s3, s4, s5, s6, special = [], [], [], [], [], [], []
maximum = n * 2 - 1
i, temp = 1, 1
ii = n
while i <= n:
    s1.append(" " * ((maximum - temp) // 2) + str(i) * temp + " " * ((maximum - temp) // 2))
    s2.append(" " * ((maximum - temp) // 2) + str(ii) * temp + " " * ((maximum - temp) // 2))
    i += 1
    ii -= 1
    temp += 2
s4 = s1[::-1]
if check:
    mid = n // 2 + 1
else:
    mid = n // 2
i = 1
temp -= 2
while i <= mid:
    s3.append(" " * ((maximum - temp) // 2) + str(i) * temp + " " * ((maximum - temp) // 2))
    temp -= 2
    i += 1
if check:
    i -= 2
else:
    i -= 1
while i > 0:
    s3.append(" " * ((maximum - temp) // 2) + str(i) * temp + " " * ((maximum - temp) // 2))
    temp -= 2
    i -= 1
i = n * 2 - 1
while i > 0:
    s1.append(" " * maximum)
    s2.append(" " * maximum)
    s3.append(" " * maximum)
    s4.append(" " * maximum)
    i -= 1
i, temp = 1, n
s, ss = "", ""
while i <= n:
    s += str(i)
    ss += str(temp)
    s5.append(s + " " * (n - len(s)))
    s6.append(ss + " " * (n - len(ss)))
    special.append(ss[::-1] + " " * (n - len(ss)))
    i += 1
    temp -= 1
s5 += s5[:-1][::-1]
s6 += s6[:-1][::-1]
special += special[:-1][::-1]
i = n * 2 - 1
temp1 = 0
while i > 0:
    print(s1[temp1] + "   " + s2[temp1] + "   " + s3[temp1] + "   " + s4[temp1] + "   " + s5[temp1] + "   " +
          s6[temp1] + "   " + s5[temp1][::-1] + "   " + s6[temp1][::-1])
    temp1 += 1
    i -= 1
print()

s1, s2, s3, s4, s5, s6, special = [], [], [], [], [], [], []
height = n * 2 - 1
maximum = len(str(n)) * n + (n - 1)
i = 1
while i <= n:
    t = [str(i)] * i
    s1.append(" " * ((maximum - (i * 2 - 1)) // 2) + " ".join(t) + " " * ((maximum - (i * 2 - 1)) // 2))
    i += 1
i, temp1 = n, 1
while i >= 1:
    t = [str(i)] * temp1
    s2.append(
        " " * ((maximum - (temp1 * 2 - 1)) // 2) + " ".join(t) + " " * ((maximum - (temp1 * 2 - 1)) // 2))
    temp1 += 1
    i -= 1
s3, s4 = s2[::-1], s1[::-1]
i = height - len(s1) + 2
while i > 0:
    s1.append(" " * maximum)
    s2.append(" " * maximum)
    s3.append(" " * maximum)
    s4.append(" " * maximum)
    i -= 1
if check:
    length = (n + 1) // 2 * 2 - 1
else:
    length = (n // 2 + 1) * 2 - 1
s, ss, i = "", "", n
sss, ssss = "", ""
while i > 0:
    if i % 2 == 1:
        s += str(i)  # 531
    else:
        ss += str(i)  # 642
    i -= 1
sss, ssss = s[::-1], ss[::-1]
if not check:
    ss += "0"
    s, ss = ss, s
i, temp = 0, 0
while i <= length:
    if i % 2 == 1:
        s5.append(" ".join(s[:temp]) + " " * (length - i))
        s6.append(" ".join(sss[:temp]) + " " * (length - i))
    else:
        s5.append(" " + " ".join(ss[:temp]) + " " * (length - i))
        s6.append(" " + " ".join(ssss[:temp]) + " " * (length - i))
        temp += 1
    i += 1
if not check:
    s6[-1]+=" "+str(n+1)
s5 += s5[:-1][::-1]
s6 += s6[:-1][::-1]
s5.pop(0)
s6.pop(0)
"""
6             1
 5             2
6 4           1 3
 5 3           2 4
6 4 2         1 3 5
 5 3 1         2 4 6
6 4 2 0       1 3 5 7
 5 3 1         2 4 6
6 4 2         1 3 5
 5 3           2 4
6 4           1 3
 5             2
6             1
"""
# i = 1
# while i <= n:
#     temp = i
#     s = ""
#     if check:
#         while temp >= 1:
#             s += str(temp) + " "
#             temp -= 2
#     else:
#         while temp >= 0:
#             s += str(temp) + " "
#             temp -= 2
#     special.append(s)
#     i += 1
# special += special[:-1][::-1]
"""
我設定奇偶輸入會這樣排
輸入6： 輸入5：
1      1
20     2 
31     31
420    42
531    531 
6420   42 
531    31
420    2
31     1
20 
1
"""
s5.pop()
s6.pop()
# print(s6,s5)
height = len(s5)
i, temp1, temp2 = 0, 0, 0
while i < height:
    print(s1[temp1] + "   " + s2[temp1] + "   " + s3[temp1] + "   " + s4[temp1] + "   " + s5[temp1] + "   " +
          s6[temp1] + "   " + s5[temp1][::-1] + "   " + s6[temp1][::-1])
    temp1 += 1
    i += 1
print()

s1, s2, s3, s4, s5, s6, special = [], [], [], [], [], [], []
s1_2, s2_2 = [], []
maximum = n * 2 - 1
height = n*2-1
i, temp = 1, n
while i < n:
    s1.append(str(i) * i + " " * (maximum - 2 * i) + str(i) * i)
    s2.append(str(temp) * i + " " * (maximum - 2 * i) + str(temp) * i)
    temp -= 1
    i += 1
i = 0
while i < n:
    s1.append(str(n) * maximum)
    s2.append("1" * maximum)
    i += 1
s3, s4 = s1[::-1], s2[::-1]
i = 1
ii = n
while i <= n:
    s, ss = "", ""
    temp, temp1 = i, ii
    while temp <= n:
        if temp == n:
            s += str(temp) * temp
            ss += str(temp1) * temp
        else:
            s += str(temp)
            ss += str(temp1)
        temp += 1
        temp1 -= 1
    s = s[::-1]
    ss = ss[::-1]
    s += (maximum - len(s)) * " "
    ss += (maximum - len(ss)) * " "
    s = s[::-1]
    ss = ss[::-1]
    s5.append(s)
    s6.append(ss)
    i += 1
    ii -= 1
s5 += s5[:-1][::-1]
s6 += s6[:-1][::-1]
i = len(s5) - height
while i > 0:
    s1.append(" " * (maximum))
    s2.append(" " * (maximum))
    s3.append(" " * (maximum))
    s4.append(" " * (maximum))
    i -= 1
i = len(s5)
temp1 = 0
while i > 0:
    print(s1[temp1] + "   " + s2[temp1] + "   " + s3[temp1] + "   " + s4[temp1] + "   " + s5[temp1] + "   " + s6[
        temp1] + "   " + s5[temp1][::-1] + "   " + s6[temp1][::-1])
    temp1 += 1
    i -= 1
print()

s1, s2, s3, s4, s5, s6, s7, s8 = [], [], [], [], [], [], [], []
maximum = n * 2 - 1
height = n * 2 - 1
i, ii = 1, n
while i < n:
    s1.append(" " * ((maximum - (i * 2 - 1)) // 2) + str(i) * (i * 2 - 1) + " " * ((maximum - (i * 2 - 1)) // 2))
    s2.append(" " * ((maximum - (i * 2 - 1)) // 2) + str(ii) * (i * 2 - 1) + " " * ((maximum - (i * 2 - 1)) // 2))
    i += 1
    ii -= 1
temp = n
while temp > 0:
    s1.append(str(n) * (i * 2 - 1))
    s2.append("1" * (i * 2 - 1))
    temp -= 1
s3 = s1[::-1]
s4 = s2[::-1]
i = n
ii = 1
while i >= 1:
    s, ss = "", ""
    temp, temp1 = n, 1
    while temp >= i:
        if temp == n:
            s += str(temp) * temp
            ss += str(temp1) * temp
        else:
            s += str(temp)
            ss += str(temp1)
        temp -= 1
        temp1 += 1
    temp, temp1 = s[::-1], ss[::-1]
    temp += (maximum - len(s)) * " "
    temp1 += (maximum - len(s)) * " "
    s += (maximum - len(s)) * " "
    ss += (maximum - len(ss)) * " "
    s5.append(s)
    s6.append(ss)
    s7.append(temp)
    s8.append(temp1)
    i -= 1
    ii += 1
s5 += s5[:-1][::-1]
s6 += s6[:-1][::-1]
s7 += s7[:-1][::-1]
s8 += s8[:-1][::-1]
i = len(s5) - height
while i > 0:
    s1.append(" " * maximum)
    s2.append(" " * maximum)
    s3.append(" " * maximum)
    s4.append(" " * maximum)
    i -= 1
i = len(s5)
temp1 = 0
while i > 0:
    print(s1[temp1] + "   " + s2[temp1] + "   " + s3[temp1] + "   " + s4[temp1] + "   " + s5[temp1] + "   "
          + s6[temp1] + "   " + s5[temp1][::-1] + "   " + s6[temp1][::-1])
    temp1 += 1
    i -= 1
print()
