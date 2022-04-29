N = int(input())
for n in range(1,N+1):
    arr = list(map(int,input().split()))
    C = max(arr)
    tmp = 0
    for a in arr:
        if a!=C:
            tmp += a**2
    print(f'Scenario #{n}:')
    if tmp==C**2:
        print('yes')
    else:
        print('no')
    print('')