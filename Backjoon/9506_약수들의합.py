while True:
    N = int(input())
    if N == -1:
        break
    arr = []
    for i in range(1,N):
        if not N%i:
            arr.append(i)
    if sum(arr)==N:
        s = ''
        print(f'{N} =',end=' ')
        for a in arr:
            s+=f'{a} + '
        print(s[0:len(s)-3])
    else:
        print(f'{N} is NOT perfect.')