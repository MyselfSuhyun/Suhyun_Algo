N, M , K = map(int,input().split())

if N == M == K:
    print(10000+N*1000)
elif N==M:
    print(1000+N*100)
elif M ==K:
    print(1000+M*100)
elif K == N:
    print(1000+K*100)
else:
    print(100*max(N,M,K))
