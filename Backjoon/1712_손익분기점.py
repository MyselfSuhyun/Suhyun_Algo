# 1712. 손익분기점
# A 만원의 고정비용
# B 만원의 가변비용
# C 만원의 노트북가격
A, B, C = map(int,input().split())

# A + N * B < N * C 를 성립할 때, 멈춘다.
# N > A/(C-B)
if C==B:
    print(-1)
else:
    N = A/(C-B)
    if N>0:
        print(int(N)+1)
    else:
        print(-1)