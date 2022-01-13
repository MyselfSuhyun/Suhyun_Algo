def solution(answers):
    answer = []
    # 총 answers 의 길이
    l = len(answers)
    # a 수포자, b 수포자, c 수포자의 답안을 가져온다.
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5] 
    c = [3,3,1,1,2,2,4,4,5,5] 
    # dict_ans 를 활용하여, 몇개 맞춘지 확인한다.
    dict_ans = {1:0,2:0,3:0}
    for i in range(l):
        # a 의 답안이 answer 와 일치하면 a의 정답 추가
        if a[i%len(a)] == answers[i]:
            dict_ans[1] += 1
        # b 의 답안이 answer 와 일치하면 b의 정답 추가
        if b[i%len(b)] == answers[i]:
            dict_ans[2] += 1
        # c 의 답안이 answer 와 일치하면 c의 정답 추가
        if c[i%len(c)] == answers[i]:
            dict_ans[3] += 1
    
    # dict item을 가져와, max값과 일치한경우, 많이 맞힌 사람이다.
    for k, v in dict_ans.items():
        if v == max(dict_ans.values()):
            answer.append(k)
    
    return answer