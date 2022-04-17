N = int(input())
Pictures = []
minimum = 36
rst1 = rst2 = 0

for i in range(N):
    tmp = [input() for _ in range(5)]
    Pictures.append(tmp)

for p1 in range(N):
    for p2 in range(p1+1,N):
        cnt = 0
        for r in range(5):
            for c in range(7):
                if Pictures[p1][r][c] != Pictures[p2][r][c]:
                    cnt +=1
        if minimum > cnt:
            minimum = cnt
            rst1 = p1
            rst2 = p2
print(f'{rst1+1} {rst2+1}')