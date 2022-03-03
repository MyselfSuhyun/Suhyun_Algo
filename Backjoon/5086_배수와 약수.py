while True:
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break
    arr = []
    for i in range(1,M+1):
        if not M%i:
            arr.append(i)
    if N in arr:
        print('factor')
        continue
    tmp = M
    while N >= tmp:
        if tmp == N:
            print('multiple')
            break
        tmp += M
    else:
        print('neither')