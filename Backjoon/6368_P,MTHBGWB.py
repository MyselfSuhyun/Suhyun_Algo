# 알파벳을 문자열로 접근하자.
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?'
# 모스 부호를 리스트로 접근하자.
mos = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','..--','---.','.-.-','----']

# 알파벳과 모스부호의 index는 동일하다. 우선 답안지를 구하고, 역순으로 해보자

# 테스트케이스의 수 T
T = int(input())
for tc in range(1,T+1):
    # 문자열을 입력받고
    S = input()
    # 인코딩된 모스부호 길이를 저장할 함수 (mos length)
    ml = []
    # 모스부호로 전환한 문자열을 받아줄 tmp
    tmp = ''

    for s in S:
        tmp += mos[alpha.index(s)]
        ml.append(len(mos[alpha.index(s)]))
        # print(s,mos[alpha.index(s)])

    # 답을 출력하자
    answer = ''

    # 현재 인덱스의 위치
    idx = 0
    # 슬라이싱으로 접근하여 decode를 하자.
    for m in ml[::-1]:
        answer += alpha[mos.index(tmp[idx:idx+m])]
        idx += m

    # 최종 decode 한 문장 출력
    print(f'{tc}: {answer}')
