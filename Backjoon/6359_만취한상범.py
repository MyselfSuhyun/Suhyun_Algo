T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [0]*(N+1)
    for i in range(2,N+1):
        for j in range(i,N+1,i):
            if arr[j]:
                arr[j]=0
            else:
                arr[j]=1
    print(arr.count(0)-1)