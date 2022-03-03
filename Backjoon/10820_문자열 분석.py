# 10820. 문자열 분석
import sys
input = sys.stdin.readline

while True:
    S = input().rstrip('\n')
    count = [0,0,0,0]
    if not S:
        break
    for s in S:
        if 'A'<=s<='Z':
            count[1] +=1
        elif 'a'<=s<='z':
            count[0] +=1
        elif '0'<=s<='9':
            count[2] +=1
        else:
            count[3]+=1
    print(*count)