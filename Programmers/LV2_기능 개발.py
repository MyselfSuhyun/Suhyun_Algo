def solution(progresses, speeds):
    stack = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]: # 작업 진도와 작업속도의 나머지, 즉 남은 작업진도 > 작업 속도 일 때,
            stack.append(int((100-progresses[i])/speeds[i]+1)) # stack 에 +1 을 더 더한 값을 append 한다.
        # 작업 진도가 작업 속도에 딱 맞게 끝낼 경우,
        else:
            stack.append(int((100-progresses[i])/speeds[i])) # stack 의 그 일수를 그대로 append한다.
    # 후에 stack의 값을 돌면서, answer 을 append 할껀데, 마지막에 나올 수 없는 최대값을 이용하여 짜투리도 바로 append해주기 위해
    stack.append(10000000)
    # answer 빈배열, count 1부터시작, tmp 는 0 의 값을 가져와서 시작한다.
    answer = []
    count = 1
    tmp = stack[0]
    # stack 의 길이만큼 돌되, tmp가 stack[0] 부터 시작하므로, 반복문은 1부터 시작한다.
    for i in range(1,len(stack)):
        # tmp 가 stack[i] 값보다 작을경우, 한번 배포해야된다. tmp 에 stack[i] 의 값을 넣어주고, count 를 append 해준 뒤, 1로 초기화 해주자.
        if tmp < stack[i]:
            tmp = stack[i]
            answer.append(count)
            count = 1
        # 아닌 경우, 한번에 배포되야하는 일이다 +=1 해주자.
        else:
            count += 1
    # 결과를 반환 한다.
    return answer