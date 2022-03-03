# 잔돈으로 나올수 있는 수를 배열에 넣어두자.
money = [500,100,50,10,5,1]

# 물품의 가격
N = int(input())

# 거슬러 줘야하는 돈
tmp = 1000 - N

# 잔돈의 개수
answer = 0

# 줄 수 있는 잔돈 지폐를 돌면서, 개수를 센다.
for m in money:
    answer += tmp // m
    # 나누고 남은 잔돈을 tmp 에 대입하고 반복문을 반복한다.
    tmp = tmp % m

# 최종 잔돈의 개수를 출력한다.
print(answer)

