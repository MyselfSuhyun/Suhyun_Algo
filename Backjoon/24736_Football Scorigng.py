point = [6,3,2,1,2]
result = []
for _ in range(2):
    arr = list(map(int,input().split()))
    rst = 0
    for a in range(len(arr)):
        rst += arr[a]*point[a]
    result.append(rst)
print(*result)