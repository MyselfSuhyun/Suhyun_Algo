T = int(input())
for _ in range(T):
    S = input()
    g=b=0
    for s in S:
        if s=='g' or s=='G':
            g+=1
        elif s=='b' or s=='B':
            b+=1
    rst = ''
    if g>b:
        rst = 'GOOD'
    elif g==b:
        rst = 'NEUTRAL'
    else:
        rst = 'A BADDY'
    print(f'{S} is {rst}')