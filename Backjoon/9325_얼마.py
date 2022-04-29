T = int(input())
for tc in range(1,T+1):
    N = int(input())
    K = int(input())
    for _ in range(K):
        p,q = map(int,input().split())
        N += p*q
    print(N)