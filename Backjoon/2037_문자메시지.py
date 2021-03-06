# 알파벳 문자의 위치
arr = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
# 알파벳 버튼을 연속으로 누르는 횟수
push = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,4,1,2,3,1,2,3,4]

# p : 버튼을 한번 누르는 데 걸리는 시간
# q : 같은 버튼을 연속으로 누를 때 걸리는 시간(C 를 입력하려면, q가 2번)
p, w = map(int,input().split())

# S : 문자 메시지
S = input()

# 걸리는 시간을 담을 int 형 answer
answer = 0

# S 를 반복문을 돌면서 걸리는 시간을 더해준다.
for i in range(len(S)):
    # 공백일 경우, p 의 시간만 추가한다.
    if S[i] == ' ':
        answer += p
    # 이전에 누른 것과 문자열이 같은 휴대폰 자판에 위치할 경우,
    # ord(' ') 은 32 로써, 이를 대입해 배열에 넣을 경우 범위를 초과한다. 따라서 조건문으로 거르자.
    elif i != 0 and S[i-1] !=' ' and arr[ord(S[i])-ord('A')] == arr[ord(S[i-1])-ord('A')]:
        # w 만큼의 지연시간이 생긴다. 동일한 번호에 있으므로
        answer += p * push[ord(S[i])-ord('A')] + w
    # 그 외의 경우, 다른 문자로 넘어가는 경우
    else:
        # 번호 입력만큼 곱하여 더해준다.
        answer += p * push[ord(S[i])-ord('A')]

# 출력할 문자메시지 보내는데 걸리는 시간을 출력한다.
print(answer)
