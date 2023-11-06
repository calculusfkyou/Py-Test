def main():
    n = int(input())
    if n > 9 or n < 1:
        print()
    else:
        if n == 1:
            print("1         x 9 +  2 = 11        \n12        x 9 +  3 = 111       ")
        elif n == 9:
            print("12345678  x 9 +  9 = 111111111 \n123456789 x 9 + 10 = 1111111111")
        else:
            nums = [n - 1, n, n + 1]
            for i in range(len(nums)):
                temp = ""
                for j in range(1, nums[i] + 1):
                    temp += str(j)
                if nums[i]==9:
                    temp="123456789 x 9 + 10 = 1111111111"
                else:
                    temp += " " * (10 - nums[i]) + "x 9 +  " + str(nums[i] + 1) + " = " + "1" * (nums[i] + 1) + " " * (
                                10 - (nums[i] + 1))
                print(temp)


if __name__ == "__main__":
    main()
