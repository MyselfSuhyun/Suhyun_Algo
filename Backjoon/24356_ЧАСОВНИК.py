t1, m1, t2, m2 = map(int,input().split())

s = t1*60+m1
e = t2*60+m2
if e-s < 0:
    tmp = 1440 + (e-s)
else:
    tmp = e-s

print(tmp,tmp//30)