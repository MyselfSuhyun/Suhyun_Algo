M = int(input())
N = int(input())
sieve = [True]*(N+1)
sieve[1] = False
i = 2
while i*i <= N:
    if not sieve[i]:
        i+=1
        continue
    for j in range(i*i,N+1,i):
        sieve[j] = False

    i += 1

ans = []
for k in range(M,N+1):
    if sieve[k]:
        ans.append(k)
if ans:
    print(sum(ans))
    print(ans[0])
else:
    print(-1)