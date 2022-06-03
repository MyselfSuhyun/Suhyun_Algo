arr = [int(input()) for _ in range(8)]
result = sorted(arr,reverse=True)
rst = 0
rar = []
for r in result[:5]:
    rst += r
    for i in range(len(arr)):
        if arr[i]==r:
            rar.append(i+1)
            break
rar.sort()
print(rst)
print(*rar)