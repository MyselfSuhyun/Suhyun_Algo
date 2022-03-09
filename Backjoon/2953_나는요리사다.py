arr = [sum(list(map(int,input().split()))) for _ in range(5)]
result = -1
r_idx = 0
for a in range(len(arr)):
    if result < arr[a]:
        result = arr[a]
        r_idx = a

print(r_idx+1,result)
