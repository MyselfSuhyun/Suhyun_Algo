N, W, H = map(int,input().split())
K = (W**2+ H**2)**(1/2)
for _ in range(N):
    N = int(input())
    if N<=K:
        print('DA')
    else:
        print('NE')