X, L, R = map(int,input().split())
result = 0xffffff
answer = 0
arr = [i for i in range(L,R+1)]

for a in arr:
    if abs(X-a) <=result:
        result = abs(X-a)
        answer = a
print(answer)