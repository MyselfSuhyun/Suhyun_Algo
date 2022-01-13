def solution(s):
    # 스택으로 풀이해보자
    stack = []
    # 문자열을 반복문으로 돌려 확인하자
    for i in s:
        # 스택이 존재하지 않으면 바로 append 
        if not stack: 
            stack.append(i)
        # 이전에 있던 값과, 문자열이 일치하면 stack 에서 pop 한다.
        elif stack[-1] == i: 
            stack.pop()
        # 일치하지 않을 경우, append 해준다.
        else: 
            stack.append(i)
    # stack 이 존재하면,  제거하지 못했다. 0을 반환
    if stack: 
        return 0
    # 존재하지 않으면, 제거를 다 했다. 1을 반환
    else: 
        return 1 