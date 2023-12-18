# v1
fibo = lambda n: 1 if n <= 1 else fibo(n - 1) + fibo(n - 2);
(lambda n: print(''.join(chr(i) for i in [ord(n[j]) + fibo(j + 1) for j in range(len(n))])[::-1]))(input()[::-1])


# v2
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def encrypt_message(message):
    reversed_message = message[::-1]
    encrypted_chars = [ord(reversed_message[j]) + fibonacci(j + 1) for j in range(len(reversed_message))]
    encrypted_string = ''.join(chr(i) for i in encrypted_chars)[::-1]
    print(encrypted_string)


user_input = input()  # 讀取用戶輸入的消息
encrypt_message(user_input)  # 加密並輸出結果


# v3
def f(n):
    if n <= 1:
        return 1
    return f(n - 1) + f(n - 2)


s = input()
s = s[::-1]
temp = ""
for i in range(len(s)):
    temp += chr(ord(s[i]) + f(i + 1))
print(temp[::-1])
