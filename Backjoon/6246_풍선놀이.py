N, Q = map(int,input().split())
visited = [0]*(N+1)
for _ in range(Q):
    L, I = map(int,input().split())
    for i in range(L,N+1,I):
        visited[i]=1
print(visited.count(0)-1)