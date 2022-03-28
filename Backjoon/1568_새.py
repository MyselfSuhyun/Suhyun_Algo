N = int(input())
cnt = 0
rst = 1
while N>0:
    if N < rst :
        rst = 1
    N -= rst
    rst +=1
    cnt +=1
    print(N,rst,cnt)

print(cnt)