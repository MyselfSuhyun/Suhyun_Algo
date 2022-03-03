N = int(input())
arr = list(map(int,input().split()))
card = dict()

for a in arr:
    if card.get(a):
        card[a] +=1
    else:
        card[a] = 1

M = int(input())
result = list(map(int,input().split()))
for r in result:
    if card.get(r):
        print(card[r],end=' ')
    else:
        print(0,end=' ')