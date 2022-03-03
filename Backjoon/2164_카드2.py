from collections import deque

N = int(input())
arr = deque([i for i in range(N,0,-1)])

while len(arr)!=1:
    arr.pop()
    arr.appendleft(arr.pop())
print(*arr)