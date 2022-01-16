N = int(input())
result = -1
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    dict_val = {1:0,2:0,3:0,4:0,5:0,6:0}
    for j in range(3):
        dict_val[arr[i][j]]+=1
    for k,v in dict_val.items():
        if v==3:
            if result < 10000+k*1000:
                result = 10000 + k * 1000
        elif v==2:
            if result < 1000 + k*100:
                result = 1000 + k* 100
        else:
            if result < k*100:
                result = k* 100
print(result)