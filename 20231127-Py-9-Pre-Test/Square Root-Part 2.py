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

n = list(map(int, input().split()))
result = 0
if n[0] ** 0.5 - int(n[0] ** 0.5) != 0:
    while len(n) > 1:
        result += int(str(n[0] ** 0.5)[n[1] + 1])
        n = n[:1] + n[2:]
else:
    result = 0
print(result)
