N = int(input())
arr = [int(input()) for _ in range(N)]
cnt = 0
while True:
    tmp = max(arr)
    if arr[0]==tmp and arr.count(tmp)==1:
        break
    for i in range(1,N):
        if arr[i]==tmp:
            arr[i]-=1
            arr[0]+=1
            cnt +=1
            break
print(cnt)