T = int(input())

for _ in range(T):
    arr = list(map(int,input().split()))
    N = arr[0]
    avg= sum(arr[1:])/N
    rst = 0
    for i in range(1,N+1):
        if arr[i]>avg:
            rst +=1
    print(f'{round(rst/N*100,3):.3f}%')
