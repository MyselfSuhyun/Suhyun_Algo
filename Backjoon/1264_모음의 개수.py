# 모음을 담고 있는 배열
gather = ['a','e','i','o','u','A','E','I','O','U']

# 입력을 계속 받으며 #이 나오면 출력을 종료한다.
while True:
    S = input()
    if S == '#':
        break

    # 모음의 갯수를 출력할 숫자형 answer 를 할당한다.
    answer = 0

    # 문자열을 돌면서, 모음의 갯수를 count 한다.
    for s in S:
        # 문자열 하나가 모음인지 확인하기 위한 조건문
        if s in gather:
            answer += 1

    # 모음의 개수를 출력한다.
    print(answer)
