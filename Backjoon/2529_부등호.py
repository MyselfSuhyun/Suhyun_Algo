N = int(input())
arr = list(input().split())
def solve(n):
    if n>=2:
        if arr[n-2]=='<':
            if num[n-2] > num[n-1]:
                return
        if arr[n-2]=='>':
            if num[n-2] < num[n-1]:
                return
    if N+1 == n:
        tmp = "".join(map(str,num))
        result.append(tmp)
        return
    for i in range(M):
        if visited[i] == 1:
            continue
        num[n]=i
        visited[i] = 1
        solve(n+1)
        visited[i] = 0


M = 10
visited = [0]*M
result = []
num = [0]*(N+1)

solve(0)
# print(result)
print(result[-1])
print(result[0])