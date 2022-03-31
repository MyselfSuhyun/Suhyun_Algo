N = int(input())
alpha = dict()
for _ in range(1,N+1):
    S = input()
    if alpha.get(S[0]):
        alpha[S[0]]+=1
    else:
        alpha[S[0]]=1
result = []
for k in alpha.keys():
    if alpha[k]>=5:
        result.append(k)
if result:
    print(sorted(result))
else:
    print('PREDAJA')