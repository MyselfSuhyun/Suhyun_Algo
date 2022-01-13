N = int(input())
R = N-100
if R<0:
    R = 1

for i in range(R,N):
    rst = i
    n = i
    while n//10:
        rst += n%10
        n//=10
    rst += n
    if N==rst:
        print(i)
        exit()
else:
    print(0)
