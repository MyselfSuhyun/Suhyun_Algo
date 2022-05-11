arr = [[0]*100 for _ in range(100)]
N, M = map(int,input().split())
for _ in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1-1,y2):
        for x in range(x1-1,x2):
            arr[y][x] +=1
rst = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] > M:
            rst+=1
print(rst)