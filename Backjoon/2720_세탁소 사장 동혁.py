T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = {25:0,10:0,5:0,1:0}
    for k in result.keys():
        while N>=k:
            N -= k
            result[k]+=1
    print(*result.values())