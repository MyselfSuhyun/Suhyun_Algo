S = list(input())
bomb = list(input())

stack = []

for i in range(len(S)):
    stack.append(S[i])
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb: # 폭탄 문자열을 만났을 경우
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')