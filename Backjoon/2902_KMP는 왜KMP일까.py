# 2902. KMP는 왜 KMP 일까?
# S: 입력받은 문자열

S = input()
result = ''
for s in S:
    if 'A'<=s<='Z':
        result +=s
print(result)