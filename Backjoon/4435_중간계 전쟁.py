# 간달프의 군대 배열
gandalf = [1,2,3,3,4,10]
# 사우론의 군대 배열
sauron = [1,2,2,2,3,5,10]

# 첫줄에 전투의 개수 T
T = int(input())
for t in range(1,T+1):
    # 간달프의 군대
    arr_G = list(map(int,input().split()))
    # 사우론의 군대
    arr_S = list(map(int,input().split()))

    # 간달프의 군대 점수
    score_G = 0
    # 사우론의 군대 점수
    score_S = 0

    for i in range(len(arr_G)):
        # 군대점수에, 해당 배열들의 곱을 더해준다.
        score_G += arr_G[i]*gandalf[i]
    for j in range(len(arr_S)):
        score_S += arr_S[j]*sauron[j]

    # 출력할 문장
    answer =''
    # 간달프의 군대가 이긴 경우
    if score_G > score_S:
        answer = 'Good triumphs over Evil'
    # 무승부인 경우
    elif score_G == score_S:
        answer = 'No victor on this battle field'
    # 사우론의 군대가 이긴 경우
    elif score_G < score_S:
        answer = 'Evil eradicates all trace of Good'

    # 최종 출력
    print(f'Battle {t}: {answer}')
