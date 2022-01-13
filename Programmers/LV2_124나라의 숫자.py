def solution(n):
    answer = ''
    while n:
        # 나머지가 있을경우, 그 값을 넣어주고, 3으로 나눠준다.
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
        # 나머지가 없을경우, 나눈 후에 4를 더해주고, 몫에서 -1한 값으로 다시 반복문을 돌려준다!
            answer += "4"
            n = n//3 - 1
    # 역순으로 바꿔서 출력한다.
    return answer[::-1]