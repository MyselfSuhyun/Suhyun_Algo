T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    p1 = 0
    p2 = 0
    for a in arr:
        if a[0]==a[1]:
            continue
        else:
            if a[0]=='R':
                if a[1]=='P':
                    p2 += 1
                elif a[1] == 'S':
                    p1 += 1
            elif a[0] == 'S':
                if a[1] == 'P':
                    p1 +=1
                elif a[1] =='R':
                    p2 +=1
            elif a[0]=='P':
                if a[1] == 'S':
                    p2 +=1
                elif a[1] == 'R':
                    p1 +=1
    if p1<p2:
        print('Player 2')
    elif p1==p2:
        print('TIE')
    elif p1>p2:
        print('Player 1')