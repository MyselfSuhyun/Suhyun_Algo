while True:
    n = int(input())
    if not n:
        break

    sieve = [True]*(2*n+1)
    sieve[1] = False
    i = 2
    while i*i<=2*n:
        if not sieve[i]:
            i +=1
            continue
        for k in range(i*i,2*n+1,i):
            sieve[k] = False
        i+=1
    cnt = 0
    for j in range(n+1,2*n+1):
        if sieve[j]:
            cnt +=1
    print(cnt)