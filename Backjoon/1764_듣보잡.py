# 1764. 듣보잡
# 듣도 못한 사람과 보도 못한 명단 사람이 주어진다. 듣도 보도 못한 사람의 명단을 구하라.

# N 듣도 못한 사람의 수
# M 보도 못한 사람의 수
N, M = map(int,input().split())

result = dict()
for _ in range(N):
    tmp = input()
    if result.get(tmp):
        result[tmp] +=1
    else:
        result[tmp] = 1
for _ in range(M):
    tmp = input()
    if result.get(tmp):
        result[tmp] +=1
    else:
        result[tmp] = 1
count = 0
answer = []
for k,v in result.items():
    if v == 2:
        count += 1
        answer.append(k)

print(count)
for a in sorted(answer):
    print(a)

# 시간 초과
# # 듣도 못한 사람의 배열
# hear = [input() for _ in range(N)]
# # 보도 못한 사람의 배열
# see = [input() for _ in range(M)]
#
# # 일단 정렬해보자.
# hear.sort()
# see.sort()
#
# # 결과값 변수
# result = 0
# arr = []
# for i in range(N):
#     if hear[i] in see:
#         result +=1
#         arr.append(hear[i])
# print(result)
# for a in arr:
#     print(a)