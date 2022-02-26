m, s, g = map(int,input().split())
a, b = map(float,input().split())
l, r = map(int,input().split())
lwait = l / a
rwait = r / b
if m%g:
    ls = m/g+1
else:
    ls = m/g
if m%s:
    rs = m/s/+1
else:
    rs = m/s
if ls+lwait < rs + rwait:
    print('friskus')
else:
    print('latmask')