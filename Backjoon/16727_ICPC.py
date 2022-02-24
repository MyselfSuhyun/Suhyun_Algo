p1, e1 = map(int,input().split())
e2, p2 = map(int,input().split())

p = p1 + p2
e = e1 + e2
if p > e :
    print('Persepolis')
elif p == e:
    if p1 == e2:
        print('Penalty')
    elif p1 > e2:
        print('Esteghlal')
    elif p1 < e2:
        print('Persepolis')
elif p < e:
    print('Esteghlal')