T = int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    L = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    # 두 원이 반지름의 크기가 같고, 같은 점일때
    if L == 0 and r1 == r2:
        print(-1)
    # 내접하거나 외접할때 1개가 접한다.
    elif r1+r2 == L or abs(r1-r2) == L:
        print(1)
    # 서로 다른 두점에서 만나는 경우,
    elif abs(r1-r2) < L < (r1+r2):
        print(2)
    # 안만나는경우
    else:
        print(0)