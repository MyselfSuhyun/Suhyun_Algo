N = int(input())
arr = list(map(int,input().split()))
visitied = [False]*101
rst = 0
for a in arr:
    if visitied[a]:
        rst +=1
    else:
        visitied[a] =True

print(rst)