from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
que = deque()
for _ in range(N):
    S = input().split()
    if len(S)==2:
        que.append(S[1])
    elif S[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif S[0] == 'size':
        print(len(que))
    elif S[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif S[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif S[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)