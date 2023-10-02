if __name__=="__main__":
    a,b=map(int,input().split())
    print("%d/%d%s%d"%(a,b,"餘",a%b))
    print("%d/%d%s%d" % (b,a,"餘",b % a))