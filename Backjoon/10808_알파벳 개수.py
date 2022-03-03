S = input()
alpha = dict()
for i in range(ord('a'),ord('z')+1):
    alpha[i]=0

for s in S:
    alpha[ord(s)]+=1

for v in alpha.values():
    print(v,end=' ')