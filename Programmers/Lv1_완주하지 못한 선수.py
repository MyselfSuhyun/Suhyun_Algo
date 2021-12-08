# LV1. 완주하지 못한 선수
def solution(participant, completion):
    # 참가자와 도착자 모두 정렬해준 뒤에,
    participant.sort()
    completion.sort()
    # 하나씩 비교하면서 일치하지 않으면, 그것이 완주하지 못한 선수이다.
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    # 다 돌동안 찾지 못할경우, 맨 마지막 선수가 완주하지 못한 선수이다.
    return participant[-1]