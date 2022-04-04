a, b, c = map(int,input().split())
dice = dict()
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            tmp = i+j+k
            if dice.get(tmp):
                dice[tmp] +=1
            else:
                dice[tmp] = 1
rst = max(dice.values())
for k in dice.keys():
    if dice[k]==rst:
        print(k)
        break