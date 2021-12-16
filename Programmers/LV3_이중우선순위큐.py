import heapq

def solution(operations):
    answer = []
    # 반복문으로 풀기
    for o in operations:
        # command 와 number 를 각각 받은뒤, number 만 int처리
        command, number = o.split()
        number = int(number)
        # answer 에 number append 해준후, 내림차순 정렬
        if command == 'I':
            answer.append(number)
            answer.sort()
        # 삭제 명령어, 1일 경우 최대값, -1일 경우 최솟값을 제거한다.
        else:
            if not answer:
                pass
            elif number == 1:
                answer.pop()
            else:
                answer.pop(0)
    # 최종적으로 내림차순하여 정렬한다. 이때 비어있으면 [0,0], 안비어있으면 answer 그대로 반환.
    answer.sort()
    if not answer:
        return [0,0]
    else:
        return [answer[-1],answer[0]]
