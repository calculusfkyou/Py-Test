while 1:
    try:
        n=int(input())
        if n==0:
            print()
        else:
            bottom=n*2-1
            print(" "*(n-1)+".")
            temp=n+1
            temp2=1
            for i in range(1,n-1):
                print(" "*(temp-temp2-2)+"."+" "*temp2+".")
                temp+=1
                temp2+=2
            print("."*bottom)
    except EOFError:
        break

#while True:
#    try:
#        n = int(input())
#        for i in range(1, n+1):
#            if(i == n): print('.' * (n+n-1))
#            elif(i == 1): print(' '*(n-1) + '.')
#            else: print(' '*(n-i) + '.' + ' '*(2*(i-1)-1) + '.')
#    except:
#        break
