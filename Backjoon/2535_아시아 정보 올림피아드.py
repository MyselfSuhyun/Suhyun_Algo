N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort(key=lambda x:x[2],reverse=True)
cnt = 0
rst = [0,0,0]
for n in range(N):
    if cnt==3:
        break
    if rst[arr[n][0]-1]<2:
        print(f'{arr[n][0]} {arr[n][1]}')
        rst[arr[n][0]-1]+=1
        cnt +=1
