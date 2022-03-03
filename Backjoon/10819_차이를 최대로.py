n = int(input())
arr = list(map(int, input().split()))
arr2 = [0 for i in range(n)]
visited = [False for i in range(n)]
ans = -1


def recur(cur):
    global ans
    if cur == n:
        total = 0
        for i in range(1, n):
            total += abs(arr[arr2[i]] - arr[arr2[i - 1]])
        ans = max(ans, total)
        return

    for i in range(n):
        if visited[i]:
            continue
        arr2[cur] = i
        visited[i] = True
        recur(cur + 1)
        visited[i] = False


# if cur == n : 부분은
# for i in range(n):
#    for j in range(n):
#        for k in range(n):
# 이라보면된다.

recur(0)
print(ans)