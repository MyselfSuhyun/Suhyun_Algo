# 각자의 답변을 입력해두자.
# # 1. 3차원 배열 방식
# answer= [['Adrian',['A','B','C']],['Bruno' ,['B','A','B','C']],['Goran',['C','C','A','A','B','B']]]
# # 0 은 상근이, 1 은 현진이, 2 는 창영이
#
# # 최고로 많이 맞춘사람
# answer_human = []
# # 최고로 많이 맞은 갯수
# answer_count = 0
#
# # 답 수 입력 받은 값
# N = int(input())
# # 해답지
# ans = input()
#
# for i in range(3):
#     # 맞은 갯수 임시 저장
#     tmp = 0
#     # 답지 반복
#     for j in range(N):
#         # 답지와 아이들이 찍은 답안지가 일치하면 tmp + 1 을 해준다.
#         if ans[j] == answer[i][1][j % len(answer[i][1])]:
#             tmp += 1
#     # 해당 값이 최댓 값인경우, 맞은 갯수와 아이디를 저장해주자.
#     if answer_count < tmp:
#         answer_count = tmp
#         answer_human = [answer[i][0]]
#     elif answer_count == tmp:
#         answer_human.append(answer[i][0])
#
# # 저장한 값을 출력해주자.
# print(answer_count)
# for a in answer_human:
#     print(a)
# -----------------------------------------------------------------------------------------------------------
# 2. 야옹님 방식
# 답지
ans = ['ABC','BABC','CCAABB']
name = ['Adrian','Bruno','Goran']

# 최고로 많이 맞춘사람
answer_human = []
# 최고로 많이 맞은 갯수
answer_count = 0
# 답 수 입력 받은 값
N = int(input())
# 해답지
answer = input()

# 사람들의 답지를 보자.
for i in range(3):
    # 현재 답을 맞춘 개수
    tmp = 0
    for j in range(N):
        if answer[j] == ans[i][j % len(ans[i])]:
            tmp += 1
    
    # 최고로 많이 맞춘 경우
    if answer_count < tmp:
        answer_count = tmp
        answer_human = [name[i]]
    # 최고로 많이 맞춘경우와 동일한 경우
    elif answer_count == tmp:
        answer_human.append(name[i])

# 많이 맞은 갯수와 사람의 아이디를 출력하자
print(answer_count)
for a in answer_human:
    print(a)