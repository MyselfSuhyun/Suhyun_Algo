from collections import deque

N , M = map(int,input().split())

arr = deque([i for i in range(1,N+1)])

solve = list(map(int,input().split()))

result = 0
for s in solve:
    while True:
        tmp = arr.index(s)
        if tmp == 0:
            arr.popleft()
            break
        if tmp <= len(arr)-tmp:
            arr.append(arr.popleft())
        else:
            arr.appendleft(arr.pop())
        result +=1
print(result)
