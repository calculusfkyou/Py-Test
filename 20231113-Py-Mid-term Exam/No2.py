def main():
    dic = {1: "1         x 9 +  2 = 11        ",
           2: "12        x 9 +  3 = 111       ",
           3: "123       x 9 +  4 = 1111      ",
           4: "1234      x 9 +  5 = 11111     ",
           5: "12345     x 9 +  6 = 111111    ",
           6: "123456    x 9 +  7 = 1111111   ",
           7: "1234567   x 9 +  8 = 11111111  ",
           8: "12345678  x 9 +  9 = 111111111 ",
           9: "123456789 x 9 + 10 = 1111111111"
           }
    n = int(input())
    if n == 1:
        print(dic[1])
        print(dic[2])
    elif n == 9:
        print(dic[8])
        print(dic[9])
    else:
        print(dic[n - 1])
        print(dic[n])
        print(dic[n + 1])


if __name__ == "__main__":
    main()
