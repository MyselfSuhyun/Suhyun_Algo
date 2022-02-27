# 1267. 핸드폰 요금
import sys
input = sys.stdin.readline
# 영식 요금제 30초마다 10원
# 민식 요금제 60초마다 15원

N = int(input())
arr = list(map(int,input().split()))
Y = 0
M = 0
for a in arr:
    Y += a//30*10+10
    M += a//60*15+15

if Y>M:
    print(f'M {M}')
elif Y==M:
    print(f'Y M {Y}')
else:
    print(f'Y {Y}')
