T = int(input())
arr = [int(input()) for _ in range(T)]
n = max(arr)
sieve = [True]*(n+1)
sieve[1] = False
i = 2
while i*i<=n:
    if not sieve[i]:
        i +=1
        continue
    for k in range(i*i,n+1,i):
        sieve[k] = False
    i+=1
for a in arr:
    tmp = a//2
    for i in range(tmp,n+1,1):
        if sieve[i] and sieve[a-i]:
            print(a-i,i)
            break
    # cnt = [0,0xffffff]
    # for j in range(a,1,-1):
    #     if sieve[j]:
    #         for k in range(j,1,-1):
    #             if a == j+k:
    #                 if cnt[1]-cnt[0] > j - k:
    #                     cnt = [k,j]
    # print(*cnt)