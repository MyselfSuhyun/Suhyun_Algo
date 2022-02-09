k, N, M = map(int,input().split())

if k*N <= M:
    print(0)
else:
    print(abs(M-k*N))