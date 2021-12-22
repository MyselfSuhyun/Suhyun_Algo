def solution(numbers):
    # 1부터 9까지의 합
    answer = 45
    # number을 돌면서 그 값이 존재하면 뺴준다.
    for number in numbers:
        if number in [1,2,3,4,5,6,7,8,9]:
            answer -= number
    return answer