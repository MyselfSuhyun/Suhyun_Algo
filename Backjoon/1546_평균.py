# 1546 평균
N = int(input())

arr = list(map(int,input().split()))[:N]
max_k = max(arr)

for i in range(len(arr)):
    arr[i] /= (max_k/100)

print(sum(arr)/N)