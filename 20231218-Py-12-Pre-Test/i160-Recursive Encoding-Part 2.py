# v1
# tribo = lambda n: 1 if n <= 3 else tribo(n-1)+tribo(n-2)+tribo(n-3); (lambda n: print(''.join(chr(i) for i in [ord(n[j])+tribo(j+1) for j in range(len(n))])[::-1]))(input()[::-1])

# v2
# def tribonacci(n):
#     # 計算第 n 項 Tribonacci 數列
#     if n <= 3:
#         return 1
#     else:
#         return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
#
#
# def encrypt_message(message):
#     reversed_message = message[::-1]  # 反轉輸入的消息
#     encrypted_chars = [ord(reversed_message[j]) + tribonacci(j + 1) for j in
#                        range(len(reversed_message))]  # 使用 Tribonacci 數列加密消息中的每個字符
#     encrypted_string = ''.join(chr(i) for i in encrypted_chars)[::-1]  # 將加密後的字符組成字符串，再反轉最終結果
#     print(encrypted_string)  # 輸出最終結果
#
#
# user_input = input()  # 讀取用戶輸入的消息
# encrypt_message(user_input)  # 加密並輸出結果


# v3
def f(n):
    if n <= 3:
        return 1
    return f(n - 1) + f(n - 2) + f(n - 3)


s = input()
s = s[::-1]
i = 0
temp = ""
while i < len(s):
    temp += chr(ord(s[i]) + f(i + 1))
    i += 1
print(temp[::-1])
