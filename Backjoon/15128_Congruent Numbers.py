a, b, c, d = map(int,input().split())
tmp = a/b*c/d/2
if int(tmp) == tmp:
    print(1)
else:
    print(0)