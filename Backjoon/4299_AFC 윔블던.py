A, B = map(int,input().split())

if A-B<0 or (A-B)%2 !=0:
    print(-1)
else:
    a = (A+B)//2
    b = (A-B)//2
    print(a,b)