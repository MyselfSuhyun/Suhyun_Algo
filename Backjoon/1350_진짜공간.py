N = int(input())
arr = list(map(int,input().split()))
k = int(input())
cnt = 0
for a in arr:
    if a%k:
        cnt += a//k + 1
    else:
        cnt += a//k
print(k*cnt)