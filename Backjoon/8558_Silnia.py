N = int(input())
rst =1
if N<5:
    for i in range(1,N+1):
        rst *=i
    print(rst%10)
else:
    print(0)