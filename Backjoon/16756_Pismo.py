import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))[:N]

result = 0xffffff
for i in range(0,N-1):
    min_tmp = abs(arr[i]-arr[i+1])
    if result >= min_tmp:
        result = min_tmp
print(result)
