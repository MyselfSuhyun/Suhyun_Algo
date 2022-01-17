# 학생수 N , 총시간 M
N, M = map(int,input().split())
show = set()

for i in range(N):
    k = int(input())
    for j in range(0,M+1,k):
        if j:
            show.add(j)
print(len(show))
