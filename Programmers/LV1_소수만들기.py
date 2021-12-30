#조합을 구하기 위해
from itertools import combinations

def solution(nums):
    answer = 0
    # n개중 3가지를 뽑아 리스틀 ㅗ저장하자.
    three_comb = list(combinations(nums, 3))
    for c in three_comb:
        # 해당 3가지의 값을 모두 더해주고, 나눌값은 root rst 로 하자(root rst 이상의 수로는 더 나눠볼 필요가 없다.)
        rst = sum(c)
        div = int(rst**(1/2))
        # 나머지가 없는 경우가 한번이라도 나올경우, 나누어지는 수다. 이 for 문이 끝날떄까지 break 가 안걸리면 answer+=1
        for i in range(2,div+1):
            if not rst%i:
                break
        else:
            answer+=1
    return answer