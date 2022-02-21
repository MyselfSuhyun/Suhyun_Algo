A = int(input()) # 원래 고기의 온도
B = int(input()) # 목표 온도 > A
C = int(input()) # 얼어있는 고기를 1도 데우는데 걸리는 시간
D = int(input()) # 얼어있는 고기를 해동하는데 걸리는 시간
E = int(input()) # 얼어있지 않는 고기를 1도 데이는데 걸리는 시간

result = 0
if A < 0:
    result += C*abs(A) + D
elif A==0:
    result += D
elif A> 0:
    result -= E*A
result += B * E
print(result)