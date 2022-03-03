a, c, e = map(int,input().split())
x, y, z = map(int,input().split())

if a<=x and c<=y and e<=z:
    print('A')
elif a<=2*x and c<=y and e<=z:
    print('B')
elif c<=y and e<=z:
    print('C')
elif c<=2*y and e<=z:
    print('D')
elif e<=z:
    print('E')
