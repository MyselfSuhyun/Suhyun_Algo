def solution(priorities, location):
    # 일단 index를 담고 있는 priorities 를 stack 에 담는다.
    stack = []
    for i in range(len(priorities)):
        stack.append((i,priorities[i]))
    # 출력 할 순서대로 담고 있을 answer
    answer = []
    # stack 은 모두 answer에 담긴다, 즉, stack 이 빌 경우, 모든 출력을 완료한 것이다.
    while stack:
        # stack 의 첫 값을  받아온다.
        tmp = stack[0][1]
        # 뒤에 남은 stack을 돌면서, 그 중요도가 첫값보다 클 경우, 해당 값을 append 해주고, 함수를 종료한다.
        for j in range(1,len(stack)):
            if tmp < stack[j][1]:
                stack.append(stack.pop(0))
                break
        # 모둔 반복을 하면서, 가장 큰값이 없었을 경우, answer에 append 해준다.
        else:
            answer.append(stack.pop(0))
    # 해당 answer를 반복하면서, location 과 일치하는 index 를 찾은경우, i + 1 을 반환해준다.
    for i in range(len(answer)):
        if answer[i][0]==location:
            return i+1