N = int(input())
arr = list(map(int,input().split()))
result = 0
tmp = 0
# print(arr)
for a in arr:
    if a:
        tmp +=1
        result += tmp
    else:
        tmp = 0


print(result)
