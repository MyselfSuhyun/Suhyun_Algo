s,k,h = map(int,input().split())
min_university = min(s,k,h)
if s+k+h>=100:
    print('OK')
elif s==min_university:
    print('Soongsil')
elif k==min_university:
    print('Korea')
elif h==min_university:
    print('Hanyang')