# 회전해도 그대로인 문자를 문자열에 저장하자
letters = 'IOSHZXN'

# 입력을 받자
S = input()

# 반복하면서, 회전하지 않는 문자가 나오면, NO를 바로 출력하자
for s in S:
    if s not in letters:
        print('NO')
        break
# 모두 회전문자이면 YES 를 출력하자.
else:
    print('YES')
