T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = bin(N)[::-1]
    for i in range(len(result)-1):
        if result[i]=='1':
            print(i,end=' ')
    print('')