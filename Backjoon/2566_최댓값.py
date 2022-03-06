arr =[list(map(int,input().split())) for _ in range(9)]
result = -1
rx = ry = 0
for i in range(9):
    for j in range(9):
        if result < arr[i][j]:
            result = arr[i][j]
            ry = i+1
            rx = j+1
print(result)
print(ry,rx)