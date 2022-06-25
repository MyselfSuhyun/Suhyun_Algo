N, K = map(int,input().split())

rst = []

for i in range(1,N+1):
    if not N%i:
        rst.append(i)
# print(rst)
if K>len(rst):
    print(0)
else:
    print(rst[K-1])