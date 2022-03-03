X , Y = map(int,input().split())

arr = list(map(int,input().split()))

t = X*Y

for a in arr:
    print(a-t,end = ' ')