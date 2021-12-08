# LV2. 전화번호 목록
def solution(phone_book):
    # 우선 접두어인 경우만 해당하는 것을 기억하고 있자.
    # 선택 정렬처럼 확인해보면 어떨까?
    # 정렬한번 해주고
    # phone_book.sort(key=len)
    phone_book = sorted(phone_book)
    # 폰 북의 총 길이
    N = len(phone_book)
    for i in range(N-1):
        # 시간초과의 늪ㅍ
        # for j in range(i+1,N):
        #     if phone_book[j].startswith(phone_book[i]):
        #         return False
        # sort 한뒤에 이중포문으로 따로 하지말자. 어짜피 sort 한 값은 문자열의 길이 순으로 정렬이 되니까!
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

