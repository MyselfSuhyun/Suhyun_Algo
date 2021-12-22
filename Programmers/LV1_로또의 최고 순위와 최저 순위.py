def solution(lottos, win_nums):
    answer = []
    # 0의 갯수 만큼, 등수가 변할 수 있다.
    rank = lottos.count(0)
    # lottos 와 win_nums 에서 일치하는 갯수를 구한다.
    rst = 0
    for lotto in lottos:
        if lotto in win_nums:
            rst += 1
    # 인덱스로 접근하자, 번호 일치에 따라 등수를 값으로 도출한다.
    result = [6,6,5,4,3,2,1]
    # 최고 순위와, 최저 순위를 출력한다.
    answer.extend([result[rank+rst],result[rst]])
    return answer