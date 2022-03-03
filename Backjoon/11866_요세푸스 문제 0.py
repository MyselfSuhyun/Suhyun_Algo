N , K = map(int,input().split())

# arr = [ k for k in range(1,N+1)]
# idx = 0
# result = []
# while True:
#     if len(result) == N:
#         break
#     i = 0
#     cnt = 0
#     while i < K:
#         if arr[(idx+cnt)%N] !=0:
#             i+=1
#         cnt +=1
#     idx += cnt-1
#     result.append(str(arr[(idx)%N]))
#     arr[(idx)%N] =0
# print(f'<{", ".join(result)}>')

from collections import deque
arr = deque(list(i for i in range(1,N+1)))
tmp = deque()
rst = []
while len(rst)<N:
    for i in range(K-1):
        tmp.append(arr.popleft())
        if len(arr)<K:
            arr.append(tmp.popleft())
    rst.append(arr.popleft())
    if len(arr) < K:
        arr += tmp
        tmp = deque()

rst = list(map(str,rst))
print(f'<{", ".join(rst)}>')