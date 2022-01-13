answer = 0

def dfs(numbers, target,length, cnt, num):
    global answer
    # 일치하면, answer 값을 +1 해준다.
    if cnt == length:
        if num == target: 
            answer+=1
        return
    # + 해준 값을 더해준 dfs, - 해준 값을 더해준 dfs
    dfs(numbers,target,length,cnt+1,num+numbers[cnt])
    dfs(numbers,target,length,cnt+1,num-numbers[cnt])
    
    return 

def solution(numbers, target):
    global answer
    # numbers의 길이를 n 에 넣는다.
    n = len(numbers)
    # numbers, target , 길이 를 넣어주고, 0번째를 알려줄cnt 와 저장된값 num을 넘겨 재귀해준다.
    dfs(numbers, target,n,0, 0)
    return answer