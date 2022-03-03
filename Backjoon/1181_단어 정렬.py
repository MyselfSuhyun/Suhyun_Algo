T = int(input())
arr = []
max_len = 0
for _ in range(T):
    tmp = input()
    if max_len < len(tmp):
        max_len = len(tmp)
    arr.append(tmp)

arr = list(set(arr))
arr.sort()
for i in range(1,max_len+1):
    for j in range(len(arr)):
        if len(arr[j])==i:
            print(arr[j])


