# 조합을 쓰자
from itertools import combinations

def solution(orders, course):
    answer = []
    # 코스 요리를 개수로 하자
    for c in course:
        # 딕셔너리로 개수를 count 하자.
        dict_order = {}
        # 조합을 모두 담을 리스트
        com = []
        for order in orders:       
            com += combinations(sorted(order),c)
        # 모든 배열을 돌면서, 동일 순서쌍일경우 +1 해주자.
        for i in com:
            if dict_order.get(i):
                dict_order[i]+=1
            else:
                dict_order[i] = 1
        # dict_order 가 있을 경우,
        if dict_order:
            # max_order 찾자
            max_order = max(dict_order.values())
            # max_order 가 2 이상인 경우(max가 1인경우는 계산할 필요 없다.)
            if max_order >=2:
                # k 값으로 value 에 접근하여, 해당 값이 max_order인 경우, answer에  append
                for k in dict_order.keys():
                    if max_order == dict_order[k]:
                        answer.append(''.join(k))
            
    return sorted(answer)