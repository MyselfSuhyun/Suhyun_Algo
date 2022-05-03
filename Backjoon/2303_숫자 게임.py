from itertools import combinations

T = int(input())
tmp = -1
result = 0
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    t = -1
    for a in list(combinations(arr,3)):
        if sum(a)%10>t:
            t = sum(a)%10
    if tmp<=t:
        tmp = t
        result = tc
print(result)