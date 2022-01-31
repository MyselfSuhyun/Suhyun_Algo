import sys

m, n = map(int, sys.stdin.readline().split())

sieve = [True] * (n + 1)
sieve[1] = False
i = 2
while i * i <= n:
    if not sieve[i]:
        i += 1
        continue
    for j in range(i * i, n + 1, i):
        sieve[j] = False
    i += 1

for i in range(m , n+1 ):
    if sieve[i]:
        print(i)