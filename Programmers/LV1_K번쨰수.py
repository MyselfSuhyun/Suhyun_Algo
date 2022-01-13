def solution(array, commands):
    answer = []
    # command 는 start, end 그리고 정렬후의 index를 가지므로 이를 for문을 통해 꺼내주자.
    for command in commands:
        # 명확하게 알기 위해, 각자에 속성에 맞게끔 변수를 지정해주자.
        start, end, index = command
        # result 는 start end 로 slicing 된 배열을 집어넣는다. start 지점은 -1을 해주자.
        result = array[start-1:end]
        # 오름차순으로 정렬해주기 위한 코드,
        result.sort()
        # 그 중, index에 위치한 값을 answer 에 append 해주자.
        answer.append(result[index-1])
    return answer