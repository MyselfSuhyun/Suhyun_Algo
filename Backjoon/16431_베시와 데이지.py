Br, Bc = map(int,input().split())
Dr, Dc = map(int,input().split())
Jr, Jc = map(int,input().split())

b = max(abs(Jr-Br),abs(Jc-Bc))
d = abs(Jr-Dr)+abs(Jc-Dc)
if b>d:
    print('daisy')
elif b==d:
    print('tie')
elif b<d:
    print('bessie')