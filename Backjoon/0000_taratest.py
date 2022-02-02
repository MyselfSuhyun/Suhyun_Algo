import sys

n, l = map(int, sys.stdin.readline().split())

li = [[0, 0, 0]]
for _ in range(n):
    d, r, g = map(int, sys.stdin.readline().split())
    li.append([d, r, g])

t = 0  # 시간
dis = 0  # 거리

for i in range(len(li) - 1):
    dis += li[i + 1][0] - li[i][0]  # for문 돌 때마다 거리 추가해줌
    rg = li[i + 1][1] + li[i + 1][2]  # 매 신호등마다 빨간불 + 초록불 시간 합

    if (t + dis) % rg == 0:  # 거리 + 시간 을 신호등 사이클로 나눈 몫이 0이면
        t += li[i + 1][1]  # 빨간불만큼 멈춰있어야 하니까 빨간불 초 추가해줌

    elif (t + dis) % rg < li[i + 1][1]:  # 거리 + 시간을 신호등 사이클로 나눈 몫이 빨간불일 때보다 작으면
        t += li[i + 1][1] - (li[i + 1][0] - li[i][0])  # 빨간불일 때의 시간 - 거리

    else:
        t += 0
dis += l - li[-1][0]  # 마지막 거리 추가해줌

print(t + dis)