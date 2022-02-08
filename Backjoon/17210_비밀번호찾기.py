N, M = map(int,input().split())
site = dict()
for _ in range(N):
    a, b = input().split()
    site[a] = b

for _ in range(M):
    result = input()
    print(site[result])