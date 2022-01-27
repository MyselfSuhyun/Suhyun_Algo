N = int(input())
arr = [input() for _ in range(N)]

result = ''
for j in range(len(arr[0])):
    tmp = arr[0][j]
    for i in range(1,len(arr)):
        if tmp != arr[i][j]:
            tmp = '?'
            break
    result += tmp
print(result)