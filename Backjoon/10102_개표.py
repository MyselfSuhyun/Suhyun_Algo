N = int(input())
arr = input()
alpha = {'A':0, 'B':0}
for a in arr:
    alpha[a]+=1

if alpha['A']>alpha['B']:
    print('A')
elif alpha['A']==alpha['B']:
    print('Tie')
elif alpha['A']<alpha['B']:
    print('B')