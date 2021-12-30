def solution(s):
    answer = []
    # 문자열이 하나이면? 반환은 1만된다.
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2+1):
        # 쪼갠 문자열을 저장
        m = ''
        # 나눈 문자열의 숫자가 됨
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s), i): 
            if tmp==s[j:i+j]: 
                cnt+=1 
            else: 
                if cnt!=1: 
                    m += str(cnt)+tmp 
                else: 
                    m += tmp 
                # 새로운 문자열 인식
                tmp=s[j:j+i] 
                cnt = 1 
        # 마지막 문자열 남은경우 처리해주기!
        if cnt!=1: 
            m += str(cnt)+tmp 
        else: 
            m += tmp 
        answer.append(len(m)) 
    return min(answer)
