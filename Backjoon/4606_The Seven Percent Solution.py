# 딕셔너리로 풀자. 딕셔너리 key(Character) : value(Encoding)
solution = {
    ' ':'%20',
    '!':'%21',
    '$':'%24',
    '%':'%25',
    '(':'%28',
    ')':'%29',
    '*':'%2a',
}

# '#' 을 만날 때 까지는 계속해서 출력한다.
while True:
    # 문자열을 입력 받자.
    S = input()

    # '#' 을 만나면 종료
    if S == '#':
        break

    # 나중에 출력할 문자열
    answer = ''

    # 문자열을 돌면서, answer 를 추가해주자.
    for s in S:
        # 딕셔너리에 존재하는 값인 경우
        if s in list(solution.keys()):
            answer += solution[s]
        # 존재하는 값이 아닌 경우
        else:
            answer += s

    # 최종 출력
    print(answer)


