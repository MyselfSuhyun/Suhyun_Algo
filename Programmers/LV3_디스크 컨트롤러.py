import heapq

def solution(jobs):
    T = len(jobs)
    # 반복문으로 푸는방법. 시간초과가 많이뜨고 실패도 뜬다.
    # jobs.sort(key = lambda x : x[0])
    # visited = [0]*T
    # answer = jobs[0][1]
    # visited[0] = 1
    # end = answer
    # while visited.count(0):
    #     index = -1
    #     min_job = 10000
    #     min_end = 10000
    #     for i in range(len(jobs)):
    #         tmp = jobs[i][1] + (end-jobs[i][0])
    #         if not visited[i] and end>jobs[i][0] and min_job > tmp :
    #             index = i
    #             min_job = tmp
    #             min_end = jobs[i][1]
    #     answer += min_job
    #     end += min_end
    #     visited[index] = 1
    # heapq 로 푸는 방법
    # 답을 기록할 answer, 현재 위치 now, 현재 시간 time
    answer, now, time = 0, 0, 0
    start = -1 
    heap = []
    
    while time < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        # 시작 시점(j[0]) 이 현재 작업 하는 중에 포함되면 heap 에 넣어준다.
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        # 지금할 수 있는 작업이 존재할 경우,
        if len(heap) > 0:
            job_start, job_ing = heapq.heappop(heap)
            start = now
            now += job_start
            answer += now - job_ing # 작업 요청시간부터 종료시간까지의 시간 계산
            time +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    
    return answer//T