def solve(n):
    for i in range(2,n//2+1):
        if not n%i:
            return False
    return True

M, N = map(int,input().split())

# for i in range(M,N):
#     if i!=1 and solve(i):
#         print(i)


for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)