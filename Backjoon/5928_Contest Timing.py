# 5928. Contest Timing

D, H, M = map(int,input().split())

start = 11*24*60 + 11* 60 + 11
end = D*24*60 + H * 60 + M
result = end - start
if result>=0:
    print(result)
else:
    print(-1)