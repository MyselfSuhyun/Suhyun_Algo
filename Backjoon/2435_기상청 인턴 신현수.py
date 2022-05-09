N, K = map(int,input().split())
arr = list(map(int,input().split()))
rst = []
for i in range(0,N-K+1):
    tmp = 0
    for j in range(i,i+K):
        tmp += arr[j]
    rst.append(tmp)
print(max(rst))