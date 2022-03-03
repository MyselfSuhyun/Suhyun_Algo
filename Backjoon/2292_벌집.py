# 2292. 벌집
N = int(input())

# 보자보자 1이면 1개
# 1 + 6 이면 2개
# 1 + 18 (12) 이면 3개
# 1 + 36 (18) 이면 4개
# 1 + 60 (24)
# .....
# 그러면 우리가 구하고자하는 방의 갯수는 1 + 6*N 이라할때, 1+ N 이 된다.
tmp = 1
answer = 1
while N > tmp:
    tmp += 6*answer
    answer +=1
print(answer)
