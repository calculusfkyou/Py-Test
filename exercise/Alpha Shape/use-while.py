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

i = 0
w = 97
s, ss = "", ""
while i < n:
    s += chr(w)
    if i % 2 == 1:
        ss += chr(w - 32)
    else:
        ss += chr(w)
    w += 1
    i += 1
print(s + "   " + s[::-1] + "   " + ss + "   " + ss[::-1])
print()

i = 0
while i < n:
    print(s[i] + "   " + s[::-1][i] + "   " + ss[i] + "   " + ss[::-1][i])
    i += 1
print()

multi, i, word, word2 = 1, 0, 97, 96 + n
s1, s2 = [], []
s7 = []
while i < n:
    s1.append(chr(word) * multi + " " * (n - multi))
    s2.append(chr(word2) * multi + " " * (n - multi))
    multi += 1
    word += 1
    word2 -= 1
    i += 1
if check:
    s7 = s2[::-1][:n // 2 + 1]
    temp = ord(s7[-1][0]) - 1
else:
    s7 = s2[::-1][:n // 2]
    temp = ord(s7[-1][0])
i = n // 2
while i > 0:
    s7.append(chr(temp) * i + " " * (n - i))
    temp -= 1
    i -= 1
i = 0
while i < n:
    print(s1[i] + "   " + s2[i] + "   " + s1[i][::-1] + "   " + s2[i][::-1] + "   " + s2[::-1][i] + "   " +
          s1[::-1][i] + "   " + s7[i] + "   " + s1[::-1][i])
    i += 1
print()

i = 0
while i < n:
    if i % 2 == 1:
        print(s1[i].upper() + "   " + s2[i].upper() + "   " + s1[i][::-1].upper() + "   " + s2[i][::-1].upper()
              + "   " + s2[::-1][i].upper() + "   " +
              s1[::-1][i].upper() + "   " + s7[i].upper() + "   " + s1[::-1][i].upper())
    else:
        print(s1[i] + "   " + s2[i] + "   " + s1[i][::-1] + "   " + s2[i][::-1] + "   " + s2[::-1][i] + "   " +
              s1[::-1][i] + "   " + s7[i] + "   " + s1[::-1][i])
    i += 1
print()

s1, s2, s3, s4, s5, s6 = [], [], [], [], [], []
word, word2 = 97, 96 + n
i = base
while i <= n:
    s1.append(" " * ((n - i) // 2) + chr(word) * i + " " * ((n - i) // 2))
    s2.append(" " * ((n - i) // 2) + chr(word2) * i + " " * ((n - i) // 2))
    word += 2
    word2 -= 2
    i += 2
s4 = s1[::-1]
s3 = s2[::-1]
i = n - len(s1)
while i > 0:
    s1.append(" " * n)
    s2.append(" " * n)
    s3.append(" " * n)
    s4.append(" " * n)
    i -= 1
if check:
    maximum = n // 2 + 1
else:
    maximum = n // 2
i, s, ss = 0, "", ""
word, word2 = 97, 96 + n
while i < maximum:
    s += chr(word)
    ss += chr(word2)
    s5.append(s + " " * (maximum - len(s)))
    s6.append(ss + " " * (maximum - len(ss)))
    word += 2
    word2 -= 2
    i += 1
if check:
    s5 += s5[:-1][::-1]
    s6 += s6[:-1][::-1]
else:
    s5 += s5[::-1]
    s6 += s6[::-1]
i = 0
while i < n:
    print(s1[i] + "   " + s2[i] + "   " + s3[i] + "   " + s4[i] + "   " + s5[i] + "   " + s6[i] + "   " +
          s5[i][::-1] + "   " + s6[i][::-1])
    i += 1
print()

i = 0
while i < n:
    j = 0
    temp1,temp2="",""
    while j < maximum:
        if j % 2 == 1:
            temp1+=s5[i][j].upper()
            temp2+=s6[i][j].upper()
        else:
            temp1 += s5[i][j]
            temp2 += s6[i][j]
        j += 1
    s5.append(temp1)
    s6.append(temp2)
    i += 1
s5,s6=s5[n:],s6[n:]
i = 0
while i < n:
    if i % 2 == 1:
        print(s1[i].upper() + "   " + s2[i].upper() + "   " + s3[i].upper() + "   " + s4[i].upper() + "   " +
              s5[i] + "   " + s6[i] + "   " + s5[i][::-1] + "   " + s6[i][::-1])
    else:
        print(s1[i] + "   " + s2[i] + "   " + s3[i] + "   " + s4[i] + "   " + s5[i] + "   " + s6[i] + "   " +
              s5[i][::-1] + "   " + s6[i][::-1])
    i += 1
print()

s1,s2,s3,s4,s5,s6=[],[],[],[],[],[]
