# LV2. 위장
def solution(clothes):
    cloth_dict = {}
    for cloth in clothes:
        if cloth_dict.get(cloth[1]) is None:
            cloth_dict[cloth[1]] = [cloth[0]]
        else:
            cloth_dict[cloth[1]].append(cloth[0])
    # 경우의 수를 계산 할 때, 가짓 수에 + 1 을 한 값을 곱한다.
    # 예제 1의 경우, 2 와 1개가 있으므로, 3*2 = 6 가지의 경우의 수가 나온다.
    # 이는 [], [yellowhat],[bluesunglasses],[green_turban],[yellowhat+green_turban],[bluesunglasses+green_turban]
    # 6 가지의 경우가 나오는 것을 볼 수 있다. 이 때, 모두 안입는 경우는 뺴야하므로, -1 을 해준다.
    answer = 1
    for i in cloth_dict.values():
        answer *= len(i)+1
    # 모두 안입은 경우를 제거하기 위해.
    return answer-1