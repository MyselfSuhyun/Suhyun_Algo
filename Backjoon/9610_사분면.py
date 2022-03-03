T = int(input())
arr = [list(map(int,input().split())) for _ in range(T)]

four = {
    'Q1':0, 'Q2':0,
    'Q3':0, 'Q4':0,
    'AXIS':0,
}

for a in arr:
    if a[0] == 0 or a[1] == 0:
        four['AXIS']+=1
    elif a[0]>0 and a[1]> 0:
        four['Q1']+=1
    elif a[0]<0 and a[1]>0:
        four['Q2']+=1
    elif a[0]<0 and a[1]<0:
        four['Q3']+=1
    elif a[0]>0 and a[1]<0:
        four['Q4']+=1
for k,v in four.items():
    print(f'{k}: {v}')