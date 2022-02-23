# 15921. 수찬은 마린보이야!
# 연습 기록들의 평균값 / 연습 기록들중 하나를 균일한 확률로 뽑을 때의 기댓값
# 수찬이의 연습 기록의 개수 N
N = int(input())

if N == 0:
    print('divide by zero')
else:
    # 수찬이의 연습 기록 N 개
    arr = list(map(int, input().split()))
    result = sum(arr)/N / (sum(arr)/N)
    print(f'{result:.2f}')