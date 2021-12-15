def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        # 이중 포문으로 해결해보자.
        for j in range(i+1,len(prices)):
            # 안떨어졌으니까 count +=1 ,하면서 for문 반복
            if prices[i]<=prices[j]:
                count+=1
            # 떨어졌으니까 count+=1 한번만 해주고(일딴 안떨어진게 1초는 되니까) break 날려준다.
            else:
                count+=1
                break
        # 해당 값을 answer 에 계속 더해준다.
        answer.append(count)
    return answer