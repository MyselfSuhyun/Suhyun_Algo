# 17413. 단어 뒤집기 2
S = list(input())

i = 0 # 인덱스
start = 0 # 시작지점

while i < len(S):
    if S[i] == '<': # <를 만날 경우
        i += 1
        while S[i] !='>': #닫힌 괄호를 만날 때 까지
            i +=1
        i += 1
    elif '0'<=S[i]<='9' or 'a'<=S[i]<='z':
        start = i
        while i < len(S) and ('0'<=S[i]<='9' or 'a'<=S[i]<='z'):
            i+=1
        tmp = S[start:i]
        tmp.reverse()
        S[start:i] = tmp
    else:
        i+=1
print(''.join(S))