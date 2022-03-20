arr = list(map(int,input().split()))
ans = min(arr)
while True:
    cnt = 0
    for a in arr:
        if not ans%a:
            cnt +=1
    if cnt>=3:
        print(ans)
        break
    ans+=1