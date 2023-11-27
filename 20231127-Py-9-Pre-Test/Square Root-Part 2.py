# def custom_sum(n):
#     if (n[0] ** 0.5 - int(n[0] ** 0.5) == 0) or len(n) == 1:
#         return 0
#     else:
#         return int(str(n[0] ** 0.5)[n[1] + 1]) + custom_sum(n[0:1] + n[2:])
#
#
# input_list = list(map(int, input().split()))
# result = custom_sum(input_list)
# print(result)

# n = list(map(int, input().split()))
# result = 0
# if n[0] ** 0.5 - int(n[0] ** 0.5) != 0:
#     while len(n) > 1:
#         result += int(str(n[0] ** 0.5)[n[1] + 1])
#         n = n[:1] + n[2:]
# else:
#     result = 0
# print(result)

# 100% version1
# import math
#
# x = input()
# y = [float(x) for x in x.split()]
#
# z = math.sqrt(y[0])
#
# a = "{:.15f}".format(z)
#
# sum_of_digits = 0
# for position in y[1:]:
#     if 0 < position <= len(a.split('.')[1]):
#         digit = int(a.split('.')[1][int(position) - 1])
#         sum_of_digits += digit
#
# print(sum_of_digits)

# 100% version2
# a = input().split()
# b = str(int(a[0]) ** 0.5)
# ans = 0
# if b[0] == '-':
#     b = b[3:]
# else:
#     b = b[2:]
# for i in range(1, len(a)):
#     if len(b) < int(a[i]):
#         continue
#     ans += int(b[int(a[i]) - 1])
# print(ans)
