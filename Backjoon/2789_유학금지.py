# CAMBRIDGE 를 검열 하기위해, 해당 문자열을 받는 값을 두자.
# university = 'CAMBRIDGE'
# 문자열을 배열에 넣어주자, 검열대상이면 1 아니면 0으루
university = [1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0]

# 값을 입력 받자
S = input()

# 출력할 값을 answer 에 추가해주자
answer = ''

# 문자열을 돌면서, 검열이 안될 경우, 추가해주자.
for s in S:
    # if s not in university:
    #     answer += s
    if not university[ord(s)-ord('A')]:
        answer += s

# 검열이 끝난 단어를 출력해주자.
print(answer)
