from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deq = deque()
for _ in range(N):
    S = input().split()

    if len(S)==2:
        if S[0] == 'push_back':
            deq.append(S[1])
        elif S[0] == 'push_front':
            deq.appendleft(S[1])
    elif S[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif S[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif S[0] == 'size':
        print(len(deq))
    elif S[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif S[0] =='front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif S[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)