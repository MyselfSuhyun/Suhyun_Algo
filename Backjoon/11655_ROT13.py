# 11655. ROT13
# 카이사르의 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.
# 암호화 한 다음 출력하는 프로그램을 작성하시오

S = input()
for s in S:
    if 'A' <= s <= 'Z':
        print(chr((ord(s)-ord('A')+13)%26+ord('A')),end='')
    elif 'a' <= s <= 'z':
        print(chr((ord(s)-ord('a')+13)%26+ord('a')),end='')
    else:
        print(s,end='')