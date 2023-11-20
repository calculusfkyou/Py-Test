n = input()
for i in range(len(n)):
    if i != 0:
        print(" " * i + " ".join(n[:-i]))
    else:
        print(" " * i + " ".join(n))