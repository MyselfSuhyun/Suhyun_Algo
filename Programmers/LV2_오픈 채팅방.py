def solution(record):
    user = dict()
    answer = []
    for r in record:
        # 상태에 따라 record 값을 split 한다.
        state= r.split()
        # 들어올 경우, user dictionary 에 그 uid : name 을 키쌍 매칭후, append 한다.
        if state[0] == "Enter":
            user[state[1]] = state[2]
            answer.append([state[1],"님이 들어왔습니다."])
        # 나갔을 경우, 그 uid 와 나갔음을 append한다.
        elif state[0] == "Leave":
            answer.append([state[1],"님이 나갔습니다."])
        # 변했을 경우, user 에 저장된 uid 의 name을 변경해준다.
        elif state[0] == "Change":
            user[state[1]] = state[2]
    # 결과를 출력할 result
    result = []
    for i in answer:
        # 이름과 문구를 append 한뒤 반환한다.
        result.append(f'{user[i[0]]}{i[1]}')
    return result