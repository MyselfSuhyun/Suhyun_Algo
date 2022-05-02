def solve(n,tmp):
    if tmp==100:
        cnt = 0
        for j in range(9):
            if visited[j]:
                cnt +=1
        if cnt == 7:
            for j in range(9):
                if visited[j]:
                    print(arr[j])
        return
    if tmp>100:
        return
    elif tmp<100:
        for i in range(n,9):
            if not visited[i]:
                visited[i]= True
                solve(i,tmp+arr[i])
                visited[i] = False

arr = [int(input()) for _ in range(9)]
visited = [False]*9
solve(0,0)