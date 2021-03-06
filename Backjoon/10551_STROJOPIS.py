# 1. 알고리즈 바보 방식
# # 일단 손가락 쓴거를 count 할 배열을 만들어주자
# sol = [0,0,0,0,0,0,0,0]
# # 숫자를 눌렀을 경우, 필요한 손가락 번호를 배열로 만들어두자.
# number = [7,0,1,2,3,3,4,4,5,6]
# # 영문자를 눌렀을 경우, 필요한 손가락 번호를 배열로 만들어두자. A 부터 시작
# alpha = [0,3,2,2,2,3,3,4,5,4,5,6,4,4,6,7,0,3,1,3,4,3,1,1,4,0]
# # 그외는 모두 7에다가 넣어주자.
#
# # 문자열을 받는다.
# S = input()
#
# for s in S:
#     # 숫자일 경우, int 형으로 변환하여 sol 에 count 해주자.
#     if '0'<=s<='9':
#         sol[number[int(s)]] += 1
#     # 문자일 경우, ord 를 활용하여 인덱스에 접근하자.
#     elif 'A'<=s<='Z':
#         sol[alpha[ord(s)-ord('A')]] +=1
#     # ',' 일 경우, 5번에 count 해주자.
#     elif s==',':
#         sol[5] +=1
#     # '.' 일 경우, 6번에 count 해주자.
#     elif s=='.':
#         sol[6] +=1
#     # 그 외의 경우는 7번에 모두 넣어주자.
#     else:
#         sol[7] +=1
#
# # 이제 손가락 별로 사용횟수를 출력하자
# for s in sol:
#     print(s)
# --------------------------------------------------------------------
# 2. 알고리즘 폐하 방식
# 배열을 key:value 형태로 매칭하자
key = "`1QAZ2WSX3EDC4RFV5TGB6YHN7UJM8IK,9OL.0P;/-['=]\\"
val = [0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,7,7,7,7,7]
# 출력할 배열
sol = [0]*8

# 문자열을 받자
S = input()

# 반복문을 돌면서 count 해주자.
for s in S:
    sol[val[key.index(s)]] += 1

# 출력 해주자
for s in sol:
    print(s)
