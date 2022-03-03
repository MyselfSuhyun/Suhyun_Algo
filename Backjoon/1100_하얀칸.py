# 1100. 하얀 칸
N = 8
chess = [input() for _ in range(N)]

result = 0

for i in range(N):
    if i%2:
        t = 'F'
    else:
        t = '.'
    for j in range(N):
        # print(1,chess[i][j],2,t)
        if t=='.' and chess[i][j]=='F':
            result += 1
        if t == 'F':
            t = '.'
        else:
            t = 'F'
print(result)
