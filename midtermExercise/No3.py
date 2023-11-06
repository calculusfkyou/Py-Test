sentence = input()
for i in range(len(sentence)):
    if sentence[i] == "@":
        print("@【跳1行】")
        print(1, end="")
    elif sentence[i] == "$":
        print("$【跳2行】")
        print(1)
        print(2, end="")
    elif sentence[i] == "#":
        print("#【跳3行】")
        print(1)
        print(2)
        print(3, end="")
    elif sentence[i] == "!":
        print("!【跳4行】")
        print(1)
        print(2)
        print(3)
        print(4, end="")
    elif sentence[i] == "%":
        print("%【跳5行】")
        print(1)
        print(2)
        print(3)
        print(4)
        print(5, end="")
    else:
        print(sentence[i], end="")
