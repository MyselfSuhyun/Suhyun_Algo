# 테스트 케이스의 수 T
T = int(input())

for tc in range(1,T+1):
    arr = input()
    stack = []

    for a in arr:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')