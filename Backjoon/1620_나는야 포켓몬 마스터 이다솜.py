N, M = map(int,input().split())

poke = dict()

for i in range(1,N+1):
    name = input()
    poke[name] = str(i)
    poke[str(i)] = name
for j in range(M):
    tmp = input()
    if poke.get(tmp):
        print(poke[tmp])