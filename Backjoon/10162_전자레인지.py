arr = [300,60,10]
result = [0,0,0]
N = int(input())

if N%10:
    print(-1)
else:
    for i in range(len(arr)):
        while True:
            if arr[i]<=N:
                result[i] += 1
                N -= arr[i]
            else:
                break
    print(*result)