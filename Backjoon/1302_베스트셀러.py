result = dict()
N = int(input())
for _ in range(N):
    S = input()
    if result.get(S):
        result[S]+=1
    else:
        result[S]=1
tmp = max(result.values())
rst = sorted(result.keys())
for r in rst:
    if result[r]==tmp:
        print(r)
        break