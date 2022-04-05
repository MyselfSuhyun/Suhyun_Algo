while True:
    try:
        n, k = map(int,input().split())
        rst = n
        while n>=k:
            rst += n//k
            n = n//k + n%k
        print(rst)
    except:
        break