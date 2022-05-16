N = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)

score = 0
result = 0
for i in range(0,N-1):
    score = arr[i] * arr[i+1]
    arr[i+1] = arr[i]+arr[i+1]
    result += score
print(result)