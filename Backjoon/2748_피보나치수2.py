N = int(input())
arr = [0]*1000
arr[0] = 0
arr[1] = 1
arr[2] = 1
if N<=2:
    print(arr[N])
else:
    for i in range(3,N+1):
        arr[i] = arr[i-1]+arr[i-2]
    print(arr[N])
