while True:
    S = input()
    if S =='.':
        break
    stack = []
    for s in S:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                elif stack[-1] == '[':
                    print('no')
                    break
            else:
                print('no')
                break
        elif s == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                elif stack[-1] == '(':
                    print('no')
                    break
            else:
                print('no')
                break
        else:
            continue

    else:
        if stack:
            print('no')
        else:
            print('yes')