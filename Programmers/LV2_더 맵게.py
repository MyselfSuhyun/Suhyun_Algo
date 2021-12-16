import heapq

def solution(scoville, K):
    answer = 0
    # # 반복문으로 푸는방법(효율성 테스트를 통과하지 못한다.)
    # while True:
    #     # 오름차순으로 정렬
    #     scoville.sort()
    #     # 현재 스코프지수의 길이
    #     T = len(scoville)
    #     count = 0
    #     # 반복문을 돌리면서, K 이상이 됬는지 확인한다.
    #     for i in range(T):
    #         if scoville[i]<K:
    #             break
    #         count +=1
    #     # K 이상으로 모두 올라갔을 경우, break 하고 answer 를 반환한다.
    #     if T==count:
    #         break
    #     # T = 1 즉 하나밖에 안남으면 섞을 수 없다. -1 로 answer 를 바꿔준 뒤 break 한다.
    #     elif T==1:
    #         answer = -1
    #         break
    #     # T = 2 이상 있을 경우 섞을 수 있다. pop 을 활용하여 2개를 꺼내서 공식에 따라 값을 바꿔준 뒤 append 한다.
    #     else:
    #         a = scoville.pop(0)
    #         b = scoville.pop(0)
    #         scoville.append(a+b*2)
    #         answer +=1
    # heapq 를 사용하는 방법.
    heapq.heapify(scoville)
    # 가장 최소값이 K 이하일 경우, 공식에 따라 스코프지수를 올려주어야한다.
    while scoville[0] < K:
        if len(scoville) > 1:
            # 가장 최솟값 두개를 공식에 따라 스코프지수를 올려주고, heqap 에 더해준다.
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            answer += 1
        # 1개만 남을 경우 바꿔줄 수 없다. -1 을 반환한다.
        else:
            return -1
    return answer