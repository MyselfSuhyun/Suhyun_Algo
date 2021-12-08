# LV3. 베스트 앨범
def solution(genres, plays):
    answer = []
    # genre_dict 로 장르에 따른 딕셔너리를 만들어주자, 이때 고유번호도 기록해주자.
    genre_dict = {}
    # 장르의 길이, 재생수도 동일할 것이다.
    N = len(genres)
    for i in range(N):
        if genre_dict.get(genres[i]) is None:

            genre_dict[genres[i]] = [[i, plays[i]]]
        else:
            genre_dict[genres[i]].append([i, plays[i]])
    answer_list = []
    # values 값만을 필요로하니까. value 만 가져오자.
    for v in genre_dict.values():
        # value 를 sort 하자, 이때 기준은 재생 횟수를 기준으로!
        v.sort(key=lambda g: g[1], reverse=True)
        # 총 재생횟수를 구하기 위한 형태, 여기서 값을 다더해주자.
        v_sum = 0
        for i in v:
            v_sum += int(i[1])
        # 길이가 한개일경우, 런타임 에러를 막기위해 따로 처리해주자.
        if len(v) == 1:
            answer_list.append([v_sum, [v[0][0]]])
        # 길이가 2개이상일 경우, 2개만 넣어서 append 해주자.
        else:
            answer_list.append([v_sum, [v[0][0], v[1][0]]])
    # 총 재생횟수를 기준으로 정렬해주자.
    answer_list.sort(key=lambda x: x[0], reverse=True)
    # 해당 곡 2개씩(1개일 경우는 1개) answer 에 extend 해주자.
    for r in answer_list:
        answer.extend(r[1])
    return answer