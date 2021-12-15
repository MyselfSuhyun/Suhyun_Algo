def solution(bridge_length, weight, truck_weights):
    answer = 0
    temp = [0]*bridge_length
    
    while temp:
        answer+=1
        temp.pop(0)
        if truck_weights:
            if sum(temp)+truck_weights[0]<=weight:
                temp.append(truck_weights.pop(0))
            else:
                temp.append(0)

        
    return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    tmp = []
    while truck_weights:
        print(tmp)
        if sum(tmp)+truck_weights[0]<=weight:
            tmp.append(truck_weights.pop(0))
            continue
        if len(tmp)==1:
            answer += bridge_length
            tmp.pop(0)
        else:
            temp = len(tmp)
            count =0
            while truck_weights:
                tmp.pop(0)
                count+=1
                if count ==temp:
                    answer += bridge_length + temp - 1
                    break
                if sum(tmp)+truck_weights[0]<=weight:
                    print(tmp,truck_weights[0],sum(tmp)+truck_weights[0])
                    print(count)
                    answer += bridge_length - count + 1
                    print('너 실행',answer)
                    tmp=[]
                    break

    if tmp:
        answer+= len(tmp) + bridge_length
        
    return answer