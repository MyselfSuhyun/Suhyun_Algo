n,a,b,c,d = map(int,input().split())

if n%a:
    tmpx = n//a+1
else:
    tmpx = n//a

if n%c:
    tmpy = n//c+1
else:
    tmpy = n//c
print(min(tmpx*b,tmpy*d))