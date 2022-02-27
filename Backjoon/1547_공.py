# 1547. 공
cup = [1,0,0]

N = int(input())
for _ in range(N):
    a, b = map(int,input().split())
    cup[a-1],cup[b-1] = cup[b-1],cup[a-1]
for i in range(3):
    if cup[i]:
        print(i+1)