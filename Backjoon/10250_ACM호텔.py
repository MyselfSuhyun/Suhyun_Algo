T = int(input())

for _ in range(T):
    W, H, N = map(int,input().split())
    X = N%W
    Y = N//W +1
    if not X:
        X = W
        Y -= 1
    if Y <10:
        Y = '0'+str(Y)
    print(str(X)+str(Y))

