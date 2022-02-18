k,w,m = map(int,input().split())
tmp = w-k
if tmp%m:
    print(tmp//m+1)
else:
    print(tmp//m)