N = int(input())
arr = sorted(list(map(int,input().split()))[:N])
n = arr[-1]
sieve = [True]*(n+1)
sieve[1] = False
i = 2
while i*i <= n:
    if not sieve[i]:
        i+=1
        continue
    for j in range(i*i,n+1,i):
        sieve[j] = False

    i += 1

ans = 0
for a in arr:
    if sieve[a]:
        ans +=1
print(ans)
