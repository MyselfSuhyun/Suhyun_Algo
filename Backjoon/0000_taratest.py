n, m = map(int, input().split())
arr = [0 for i in range(n)]


def recur(cur, start):
    if cur == n:
        return print(*arr)

    for i in range(start, m):
        arr[cur] = i
        recur(cur + 1, i + 1)


recur(0, 0)
