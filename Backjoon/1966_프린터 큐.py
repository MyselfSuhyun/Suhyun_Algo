from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    que = deque(list(map(int, input().split())))
    count = 0
    while que:
        b = max(que)
        start = que.popleft()
        m -= 1

        if b == start:
            count += 1
            if m < 0:
                print(count)
                break

        else:
            que.append(start)
            if m < 0 :
                m = len(que) - 1