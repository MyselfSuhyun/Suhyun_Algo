arr = list(map(int,input().split()))
tmp = max(arr)
result = 0
for a in arr:
    result += tmp - a
print(result)