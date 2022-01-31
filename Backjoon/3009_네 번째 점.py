X = dict()
Y = dict()

N = 3
for _ in range(N):
    x, y = map(int,input().split())
    if X.get(x) is None:
        X[x] = 1
    else:
        X[x] += 1
    if Y.get(y) is None:
        Y[y] = 1
    else:
        Y[y] +=1
ans = [0,0]
for kx in X.keys():
    if X[kx] == 1:
        ans[0] = kx
for ky in Y.keys():
    if Y[ky] == 1:
        ans[1] = ky
print(*ans)