# 1011. Fly me to the Alpha Centauri

T = int(input())

for _  in range(T):
    X, Y = map(int,input().split())
    L = Y - X
    cnt = 0 # 이동횟수
    tmp = 1 # 이동 가능 거리
    current = 0 # 이동 거리의 합
    while current < L:
        cnt += 1
        current += tmp
        if not cnt % 2:
            tmp +=1
    print(cnt)